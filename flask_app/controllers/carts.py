from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.product import Product
from flask_app.models.cart import Cart

@app.route('/add/<product_id>')
def add_item(product_id):
    if 'user_id' not in session:
        return redirect('/loginreg')
    data = {
        'product_id' : product_id,
        'user_id' : session['user_id']
    }
    Cart.add_item(data)
    return redirect('/view_cart')


@app.route('/view_cart')
def view_cart():
    data = {
        'user_id' : session['user_id']
    }
    x = Cart.get_cart_items(data)
    print("THIS IS THE DATA!",x)
    return render_template('cart.html', cart_items = Cart.get_cart_items(data))


@app.route("/cart/delete/<int:product_id>")
def delete_product(product_id):
    if 'user_id' not in session:
        return redirect('/logout')
    product_data = {
        'product_id': product_id,
        'user_id':session['user_id']
    }
    Cart.delete(product_data)
    return redirect('/dashboard')



