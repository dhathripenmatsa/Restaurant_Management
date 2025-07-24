from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DB_NAME = 'restaurant.db'

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(query, args)
    rv = c.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        category = request.form['category']
        query_db('INSERT INTO menu (name, price, category) VALUES (?, ?, ?)', (name, price, category))
        return redirect('/menu')
    items = query_db('SELECT * FROM menu')
    return render_template('menu.html', items=items)

@app.route('/delete_menu/<int:item_id>')
def delete_menu(item_id):
    query_db('DELETE FROM menu WHERE id = ?', [item_id])
    return redirect('/menu')

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        item = request.form['item']
        quantity = int(request.form['quantity'])
        query_db('INSERT INTO inventory (item, quantity) VALUES (?, ?)', (item, quantity))
        return redirect('/inventory')
    inventory_items = query_db('SELECT * FROM inventory')
    return render_template('inventory.html', inventory=inventory_items)

@app.route('/delete_inventory/<int:item_id>')
def delete_inventory(item_id):
    query_db('DELETE FROM inventory WHERE id = ?', [item_id])
    return redirect('/inventory')

@app.route('/sales', methods=['GET', 'POST'])
def sales():
    if request.method == 'POST':
        dishname = request.form['dishname']
        quantity = int(request.form['quantity'])
        price_row = query_db('SELECT price FROM menu WHERE name = ?', [dishname], one=True)
        if price_row:
            total = quantity * price_row[0]
            query_db('INSERT INTO sales (dishname, quantity, total) VALUES (?, ?, ?)', (dishname, quantity, total))
        return redirect('/sales')
    sales_data = query_db('SELECT * FROM sales')
    return render_template('sales.html', sales=sales_data)

@app.route('/delete_sales/<int:item_id>')
def delete_sales(item_id):
    query_db('DELETE FROM sales WHERE id = ?', [item_id])
    return redirect('/sales')

@app.route('/offers', methods=['GET', 'POST'])
def offers():
    if request.method == 'POST':
        offer = request.form['offer']
        query_db('INSERT INTO offers (description) VALUES (?)', [offer])
        return redirect('/offers')
    offer_data = query_db('SELECT * FROM offers')
    return render_template('offers.html', offers=offer_data)

@app.route('/delete_offer/<int:item_id>')
def delete_offer(item_id):
    query_db('DELETE FROM offers WHERE id = ?', [item_id])
    return redirect('/offers')

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        query_db('INSERT INTO reviews (name, comment) VALUES (?, ?)', (name, comment))
        return redirect('/reviews')
    reviews_data = query_db('SELECT * FROM reviews')
    return render_template('reviews.html', reviews=reviews_data)

@app.route('/delete_review/<int:item_id>')
def delete_review(item_id):
    query_db('DELETE FROM reviews WHERE id = ?', [item_id])
    return redirect('/reviews')

if __name__ == '__main__':
    app.run(debug=True)
