import sqlite3

DB_NAME = 'restaurant.db'

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

# Sample menu items
menu_items = [
    ('Margherita Pizza', 250.0, 'Main Course'),
    ('Veg Burger', 120.0, 'Snacks'),
    ('Cold Coffee', 90.0, 'Beverages'),
    ('Gulab Jamun', 60.0, 'Dessert')
]
c.executemany('INSERT INTO menu (name, price, category) VALUES (?, ?, ?)', menu_items)

# Sample inventory items
inventory_items = [
    ('Tomatoes', 50),
    ('Buns', 40),
    ('Milk', 30),
    ('Sugar', 60)
]
c.executemany('INSERT INTO inventory (item, quantity) VALUES (?, ?)', inventory_items)

# Sample sales
sales = [
    ('Margherita Pizza', 2, 500.0),
    ('Veg Burger', 1, 120.0)
]
c.executemany('INSERT INTO sales (dishname, quantity, total) VALUES (?, ?, ?)', sales)

# Sample offers
offers = [
    ('Buy 1 Get 1 Free on Veg Burger'),
    ('20% off on orders above ₹500')
]
c.executemany('INSERT INTO offers (description) VALUES (?)', [(o,) for o in offers])

# Sample reviews
reviews = [
    ('Anjali', 'Amazing taste and fast service!'),
    ('Rahul', 'Great ambiance and delicious food.')
]
c.executemany('INSERT INTO reviews (name, comment) VALUES (?, ?)', reviews)

conn.commit()
conn.close()

print("Sample data inserted successfully.")

