# sql_intro_2.py

import sqlite3
import pandas as pd

# Path to the database
db_path = "../db/lesson.db"

# Connect to the database
conn = sqlite3.connect(db_path)

# SQL query: join line_items and products
query = """
SELECT 
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products
    ON line_items.product_id = products.product_id;
"""

# Read data into DataFrame
df = pd.read_sql_query(query, conn)

# Print first 5 rows
print("Initial DataFrame:")
print(df.head(), "\n")

df['total'] = df['quantity'] * df['price']
print(df.head())

grouped_df = df.groupby(df['product_id']).agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'})

print(grouped_df.head())

sorted_df = grouped_df.sort_values(by='product_name')
print(sorted_df.head())


sorted_df.to_csv('order_summary.csv', index=False)


   

