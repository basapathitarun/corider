from flask_pymongo import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def from_dict(data):
        return User(
            name=data.get('name'),
            email=data.get('email'),
            password=data.get('password')
        )

    @staticmethod
    def to_dict(user):
        return {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "password": user["password"]
        }
