from itertools import product
from math import prod
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.product import Product


@app.route('/search', methods=['POST'])
def get_product_by_category():
    print(request.form['search'])
    category_info = Product.get_product_by_category(request.form['search']) 
    print(category_info)
    return redirect('/product_info')

# @app.route('/product_info')
# def product_info():
#     total_in_cart = session['count']
#     return render_template('products.html', total_in_cart = total_in_cart)

@app.route('/products/<category>')
def category_products(category):
    products = []
    title = 'products'
    if (category == 'menswear'):
        products = Product.get_product_by_category('men\'s clothing')
        title = 'Men\'s Wear'
    if (category == 'womenswear'):
        products = Product.get_product_by_category('women\'s clothing')
        title = 'Women\'s Wear'
    if (category == 'jewelery'):
        products = Product.get_product_by_category('jewelery')
        title = 'Jewelery'
    if (category == 'electronics'):
        products = Product.get_product_by_category('electronics')
        title = 'Electronics'

    total_in_cart = session['count']
    return render_template('products.html', title = title, products = products, total_in_cart = total_in_cart)

@app.route('/view/<int:num>')
def details(num):
    all = Product.get_all_products()
    for i in all:
        if num == i['id']:
            product = i
    total_in_cart = session['count']
    return render_template('details.html', product = product, total_in_cart= total_in_cart )


