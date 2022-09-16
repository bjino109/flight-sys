from flask import jsonify
from flask_restful import Resource
from models import administrators
from flask_jwt import jwt_required


class Admin_res(Resource):

    @jwt_required()
    def get(self, name):
        user = administrators.Administrators.find_by_first_Name(name)
        if user:
            return user.json()
        else:
            return jsonify({'massge': 'user not found or user not adminstator '})

    def post():
        pass

    def delete(self, name):
        user = administrators.Administrators.find_by_id(name)

        if not user:
            return jsonify({'massge': 'there is no admin with thet name'})
        user.delete_user()
        return jsonify({'massge': 'user  deleted!'})


class Admin_list(Resource):
    def get(self):
        return list(map(lambda x: x.json(), administrators.Administrators.query.all()))
