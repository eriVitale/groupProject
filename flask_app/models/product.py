# No SQL connection because this is showing what we expect from the API
import requests

class Product:
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
    def get_all_products():
        return requests.get('https://fakestoreapi.com/products').json()

    @staticmethod
    def get_product_by_category(category):
        return requests.get('https://fakestoreapi.com/products/category/' + category).json()
>>>>>>> main
