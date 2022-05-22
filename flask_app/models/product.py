from flask_app.config.mysqlconnection import connectToMySQL
import requests

class Product:
    db='estore'
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.price = data['price']
        self.description = data['description']
        self.category = data['category']
        self.image = data['image']
        self.rating = data['rating']
        self.user_id = data['user_id']

<<<<<<< HEAD
=======

    @staticmethod
    def get_product_by_category(category):
        return requests.get('https://fakestoreapi.com/products/category/' + category).json()
>>>>>>> main
