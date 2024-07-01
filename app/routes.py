from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from .models import User
from . import mongo

bp = Blueprint('routes', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify([User.to_dict(user) for user in users]), 200

@bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(User.to_dict(user)), 200
    return jsonify({"error": "User not found"}), 404

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User.from_dict(data)
    user_id = mongo.db.users.insert_one(user.__dict__).inserted_id
    return jsonify({"id": str(user_id)}), 201

@bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"msg": "User updated"}), 200

@bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({"_id": ObjectId(id)})
    return jsonify({"msg": "User deleted"}), 200



    