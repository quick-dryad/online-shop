from flask import render_template
from models import Product
from app import app

# Placeholder for product data
products = [
    Product('Product 1', 20.0),
    Product('Product 2', 30.0),
    # Add more products as needed
]

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)
