from flask import jsonify
from flask_restful import Resource
from models import users
from flask_jwt import jwt_required


class User_res(Resource):
    def get(self, name):
        user = users.Users.find_by_username(name)
        if user:
            return user.json()
        else:
            return jsonify({'massge': 'user not found'})

    def delete(self, name):
        user = users.Users.find_by_id(name)

        if not user:
            return jsonify({'massge': 'there is no user with thet id'})
        user.delete_user()
        return jsonify({'massge': 'user  deleted!'})


class User_list(Resource):
    def get(self):
        return list(map(lambda x: x.json(), users.Users.query.all()))
