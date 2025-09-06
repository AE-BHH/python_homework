import sqlite3

def create_database():
    try:

        conn = sqlite3.connect('../db/magazines.db')
        print('Connection successful.')
        
        conn.execute("PRAGMA foreign_keys = 1")

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers (
            publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            publisher_name TEXT NOT NULL UNIQUE
            )
        """)
        print('Publisher table created.')
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            magazine_name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
                       FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
            )
        """)
        print('Magazine table created.')

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_name TEXT NOT NULL,
            subscriber_address TEXT NOT NULL
            )
        """)
        print('Subscriber table created.')
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
            UNIQUE(subscriber_id, magazine_id) -- Prevent dublicate                      
            )
    """)
        print('Subscription table created.')


        conn.commit()

        return conn

    except sqlite3.Error as e:
        print(f'Some error happened: {e}')
        return None
    

def add_publisher(conn, name):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT publisher_id FROM Publishers WHERE publisher_name = ?', (name,))
        exists = cursor.fetchone()

        if exists:
            print(f'Publisher {name} already exists with ID {exists[0]}')
            return exists[0]
        else:
            cursor.execute('INSERT INTO Publishers (publisher_name) VALUES (?)', (name,))
            publisher_id = cursor.lastrowid
            print(f'Added publisher {name} with ID {publisher_id}')
            return publisher_id
    except sqlite3.Error as e:
        print(f'Error adding publisher {name}: {e}')
        return None
        

def add_magazine(conn, name, publisher_id):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT magazine_id FROM Magazines WHERE magazine_name = ?', (name,))
        exist = cursor.fetchone()

        if exist:
            print(f'Magazine {name} already exists with ID {exist[0]}')
            return exist[0]
        
        else:
            cursor.execute('INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?, ?)',( name, publisher_id))
            magazine_id = cursor.lastrowid
            print(f'{name} added with ID {magazine_id}')
            return magazine_id
        
    except sqlite3.Error as e:
        print(f"Error occurred with adding the magazine {name}")
        return None
    
def add_subscriber(conn, name, address):
    try:
        cursor = conn.cursor()

        cursor.execute('SELECT subscriber_id FROM Subscribers WHERE subscriber_name = ? AND subscriber_address = ?', (name, address))

        exist = cursor.fetchone()
        if exist:
            print(f'Entry already exists.')
            return exist[0]
        else:
            cursor.execute('INSERT INTO Subscribers (subscriber_name, subscriber_address) VALUES (?, ?)', (name, address))
            subscriber_id = cursor.lastrowid
            print('Entry added.')
            return subscriber_id

    except sqlite3.Error as e:
        print(f'Error adding subscriber {name}: {e}')
        return None
 
        
def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        cursor = conn.cursor()

        cursor.execute('SELECT subscription_id FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ?', (subscriber_id, magazine_id))

        exists = cursor.fetchone()

        if exists:
            print(f'Subscription already exists.')
            return exists[0]
        else:
            cursor.execute('INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)', (subscriber_id, magazine_id, expiration_date))

            subscription_id = cursor.lastrowid
            print('Entery added successfully')
            return subscription_id
        
        
    except sqlite3.Error as e:
        print(f'Error adding subscription: {e}')
        return None
    

def fetch_queries(conn):
    cursor = conn.cursor()

    cursor.execute('SELECT * from Subscribers')
    result = cursor.fetchall()
    for row in result:
        print(row)


    cursor.execute('Select * FROM Magazines ORDER BY magazine_name')
    magazines = cursor.fetchall()
    for row in magazines:
        print(row)

    
    cursor.execute('''SELECT m.magazine_id, m.magazine_name, p.publisher_name FROM Magazines m JOIN Publishers p ON m.publisher_id = p.publisher_id WHERE p.publisher_name = 'Free Friday' ''')
    magazines = cursor.fetchall()
    for row in magazines:
        print(row)

    
def populate_database(conn):
    try:
        pub1 = add_publisher(conn, 'Free Friday')
        pub2 = add_publisher(conn, 'Readers')
        pub2 = add_publisher(conn, 'BlueInk')

        mag1 = add_magazine(conn, '30 Minutes', pub2)
        mag2 = add_magazine(conn, 'Red Apple', pub1)
        mag3 = add_magazine(conn, 'Pine Tree', pub2)

        sub1 = add_subscriber(conn, 'Sara Morgan', '555 Sun Dr, Virginia, VA')
        sub2 = add_subscriber(conn, 'John Smith', '123 Green Dr, Salt Lake, UT')
        sub3 = add_subscriber(conn, 'Mary Alen', '667 Sun rd, Leesburg, VA')
        sub4 = add_subscriber(conn, 'Mike Johnson', '700 E 900 N, Provo, UT')

        add_subscription(conn, sub1, mag1, '2000-01-20')
        add_subscription(conn, sub2, mag2, '2010-11-07')
        add_subscription(conn, sub3, mag3, '2020-01-17')
        add_subscription(conn, sub4, mag3, '2019-12-16')

        conn.commit()
        print('Database populated successfully')

    except sqlite3.Error as e:
        print(f'Error populating database: {e}')



conn = create_database()

if conn:
    try:

        populate_database(conn)
        fetch_queries(conn)
        conn.close()
        print('Database connection closed')
    except sqlite3.Error as e:
        print(f'Error occured during population: {e}')
        conn.close()






