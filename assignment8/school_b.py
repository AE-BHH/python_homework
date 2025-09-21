import sqlite3

with sqlite3.connect('../db/school.db') as conn:
    conn.execute('PRAGMA foriegn_key = 1')

    cursor = conn.cursor()

    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Ali', 18, 'Medical')")
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Sam', 25, 'CS')")
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Mary', 22, 'BA')")

    conn.commit()