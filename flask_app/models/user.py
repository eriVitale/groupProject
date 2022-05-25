from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
import re
from flask_bcrypt import Bcrypt
from flask import flash, session
bcrypt=Bcrypt(app)
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db='estore'
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

        self.products=[]

    @classmethod
    def save(cls,data):
        print(data)
        query="INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_from_email(cls,data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        results=connectToMySQL(cls.db).query_db(query,data)
        if len(results)<1:
            return False
        else:
            return cls(results[0])
    
    @classmethod
    def get_one_from_id(cls,data):
        query="SELECT * FROM users WHERE id=%(id)s;"
        results= connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid=True
        query="SELECT * FROM users WHERE email=%(email)s;"
        results=connectToMySQL(User.db).query_db(query,user)
        if results:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address")
            is_valid=False
        if len(user['first_name'])<2 or user['first_name'].isalpha()==False:
            flash("*First name must be at least 2 characters and consist of only alphabetic characters")
            is_valid=False
        if len(user['last_name'])<2 or user['last_name'].isalpha()==False:
            flash("*Last name must be at least 2 characters and consist of only alphabetic characters")
            is_valid=False
        if len(user['password']) <8:
            flash("*Password must be at least 8 characters")
            is_valid=False
        if user['confirm_password'] != user['password']:
            flash("*Confirm Password must match Password field")
            is_valid=False
        return is_valid
    