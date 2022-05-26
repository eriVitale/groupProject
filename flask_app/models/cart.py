from click import FloatRange
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.product import Product
import requests

class Cart:
    db='estore'
    def __init__(self,data):
        self.user_id = data['user_id']
        self.product_id = data['product_id']
        self.quantity = data['quantity']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def add_item(cls, data):
        query = 'INSERT INTO cart (user_id, product_id, quantity) VALUES (%(user_id)s, %(product_id)s, 1) ON DUPLICATE KEY UPDATE quantity = quantity + 1;'
        added_item = connectToMySQL(cls.db).query_db(query, data)
        return added_item

    @classmethod
    def get_cart_items(cls, data):
        query = 'SELECT * FROM cart WHERE user_id = %(user_id)s;'
        all_products = Product.get_all_products()
        cart_items = connectToMySQL(cls.db).query_db(query, data)
        for item in cart_items:
            for product in all_products:
                if product['id'] == item['product_id']:
                    item['product_info'] = product
        return cart_items

    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM cart WHERE user_id = %(user_id)s AND product_id = %(product_id)s;'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_cart_total(cls,data):
        query="SELECT * FROM cart WHERE user_id=%(user_id)s;"
        all_products = Product.get_all_products()
        cart_items=connectToMySQL(cls.db).query_db(query,data)
        total=0
        for item in cart_items:
            for product in all_products:
                if product['id'] == item['product_id']:
                    total+=float(product['price']* cart_items['quantity'])
        total=float(total)
        return ('$'+format(total,'.2f'))

    @classmethod
    def checkout(cls,data):
        query="DELETE FROM cart WHERE user_id=%(user_id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def counter(cls , data):
        query = "SELECT SUM(quantity) as cart_total FROM cart"
        return connectToMySQL(cls.db).query_db( query , data)