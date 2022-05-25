from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.product import Product
from flask_app.models.cart import Cart

@app.route('/add/<product_id>')
def add_item(product_id):
    if 'user_id' not in session:
        return redirect('/loginreg')
    if "total" not in session:
        session['total'] = 1
    elif "total" in session:
        session['total'] += 1
    data = {
        'product_id' : product_id,
        'user_id' : session['user_id']
    }
    Cart.add_item(data)
    return redirect(request.referrer)


@app.route('/view_cart')
def view_cart():
    data = {
        'user_id' : session['user_id']
    }
    x = Cart.get_cart_items(data)
    return render_template('cart.html', cart_items = Cart.get_cart_items(data))


@app.route("/cart/delete/<int:product_id>")
def delete_product(product_id):
    if 'user_id' not in session:
        return redirect('/logout')
    if "total" in session:
        session['total'] -= 1
    elif session['total'] == 0:
        session['total'] = 0
    product_data = {
        'product_id': product_id,
        'user_id':session['user_id']
    }
    Cart.delete(product_data)
    return redirect('/view_cart')



