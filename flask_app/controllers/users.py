
from requests import Session
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.cart import Cart

from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loginreg')
def loginreg():
    return render_template('login_reg.html')

@app.route('/register',methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash=bcrypt.generate_password_hash(request.form['password'])
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':pw_hash
    }
    id=User.save(data)
    session['user_id']=id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'id': session['user_id'],
    }
    name = session['name']

    return render_template('dashboard.html', user=User.get_one_from_id(data), name = name,)

@app.route('/login',methods=['POST'])
def login():
    data={'email':request.form['email']}
    user_in_db=User.get_from_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id']=user_in_db.id
    session['name'] = user_in_db.first_name
    cart_total = Cart.counter(data)
    session['count'] = cart_total[0]['cart_total']
    print("THIS IS THE NAME" , session['name'])
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



