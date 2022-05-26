from ast import Not
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
    cart_total = Cart.counter(data)
    print("THIS IS THE COUNT",cart_total[0]['cart_total'])
    session['count'] = cart_total[0]['cart_total']
    return redirect(request.referrer)


@app.route('/view_cart')
def view_cart():
    data = {
        'user_id' : session['user_id']
    }
    x = Cart.get_cart_items(data)
    total_in_cart = session['count']
    return render_template('cart.html', cart_items = Cart.get_cart_items(data),total=Cart.get_cart_total(data), total_in_cart = total_in_cart)


@app.route("/cart/delete/<int:product_id>")
def delete_product(product_id):
    if 'user_id' not in session:
        return redirect('/logout')
    product_data = {
        'product_id': product_id,
        'user_id':session['user_id']
    }
    Cart.delete(product_data)
    cart_total = Cart.counter(product_data)
    session['count'] = cart_total[0]['cart_total']
    return redirect('/view_cart')

@app.route('/checkout')
def checkout():
    data={
        'user_id':session['user_id']
    }
    cart_total = Cart.counter(data)
    session['count'] = cart_total[0]['cart_total']
    print(session['count'])
    if not session['count']:
        return render_template('notcheckout.html')
    Cart.checkout(data)
    cart_total = Cart.counter(data)
    session['count'] = cart_total[0]['cart_total']
    return render_template('checkoutsuccess.html')



