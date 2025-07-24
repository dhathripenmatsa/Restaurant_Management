import sqlite3

conn = sqlite3.connect('restaurant.db')
c = conn.cursor()

# Drop existing tables for a clean reset (optional during development)
c.execute('DROP TABLE IF EXISTS menu')
c.execute('DROP TABLE IF EXISTS inventory')
c.execute('DROP TABLE IF EXISTS sales')
c.execute('DROP TABLE IF EXISTS offers')
c.execute('DROP TABLE IF EXISTS reviews')

# Create tables
c.execute('''
CREATE TABLE menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT
)
''')

c.execute('''
CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')

c.execute('''
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dishname TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    total REAL NOT NULL
)
''')

c.execute('''
CREATE TABLE offers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL
)
''')

c.execute('''
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    comment TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Database created with all necessary tables.")