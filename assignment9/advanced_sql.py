import sqlite3


conn = sqlite3.connect('../db/lesson.db')

cursor = conn.cursor()
print('Connected to database successfully.')

#Task 1: Complex JOINs with Aggregation

query = """
SELECT o.order_id,
ROUND(SUM(li.quantity * p.price),2) AS total_price
FROM orders AS o
JOIN line_items AS li ON o.order_id = li.order_id
JOIN products AS p
ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""

cursor.execute(query)
# print(cursor.fetchall())

conn.close()


# Task 2: Understanding Subqueries

conn = sqlite3.connect('../db/lesson.db')
cursor = conn.cursor()
# print('Connected to database successfully for the 2nd task.')


query2 = """
WITH order_avg AS (
SELECT o.order_id,
o.customer_id AS customer_id_b,
SUM(p.price * li.quantity) AS total_price
FROM orders AS o
JOIN line_items AS li
ON li.order_id = o.order_id
JOIN products AS p
ON p.product_id = li.product_id
GROUP BY o.order_id, o.customer_id
)
SELECT c.customer_name,
ROUND(AVG(oa.total_price), 2) AS cust_avg_order
FROM customers as c
LEFT JOIN order_avg AS oa
ON c.customer_id = oa.customer_id_b
GROUP BY c.customer_id
ORDER BY cust_avg_order DESC
"""

cursor.execute(query2)
# print(cursor.fetchall())

conn.close()


# Task 3: An Insert Transaction Based on Data

conn = sqlite3.connect('../db/lesson.db')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

cursor.execute("""
SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';
""")
customer_id = cursor.fetchone()[0]
cursor.execute("""
SELECT employee_id, (e.first_name || ' ' || e.last_name) as employee_name FROM employees as e
WHERE employee_name = 'Miranda Harris'; 
""")
emp_id = cursor.fetchone()[0]

least_exp_prod = """
SELECT product_id FROM products ORDER BY price ASC LIMIT 5;
"""
cursor.execute(least_exp_prod)
print(cursor.fetchall())

cursor.execute("""
INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, CURRENT_DATE)
RETURNING order_id;
""", (customer_id, emp_id))
order_id = cursor.lastrowid

cursor.execute("""
INSERT INTO line_items (order_id, product_id, quantity)
SELECT ?, product_id, 10
FROM products
ORDER BY price ASC
LIMIT 5;

""", (order_id,))

cursor.execute("""
SELECT li.line_item_id, li.quantity, p.product_name
FROM line_items AS li
JOIN products AS p 
ON li.product_id = p.product_id
WHERE li.order_id = ?
""", (order_id,))

print(cursor.fetchall())


conn.commit()
cursor.close()
conn.close()



# Task 4: Aggregation with HAVING

conn = sqlite3.connect('../db/lesson.db')
cursor = conn.cursor()

cursor.execute("""
SELECT
(e.first_name || ' ' || e.last_name) AS emp_name,
COUNT(o.order_id) AS num_order
FROM employees AS e
JOIN orders AS o
ON e.employee_id = o.employee_id
GROUP BY e.employee_id, emp_name
HAVING COUNT(o.order_id) > 5;
""")
print('Here is the list of employees who were associated more than 5 orders')
print(cursor.fetchall())

cursor.close()
conn.close()