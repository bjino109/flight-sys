from flask_restful import Resource, reqparse
from pkg_resources import require
from flask import Flask, request, make_response

from flask import jsonify
from models.users import Users
from resources.auth import Auth


def token_required(f):
    def decorator(*args, **kwargs):
        token = None
        
        if 'x-auth-token' in request.headers:
            token = request.headers['x-auth-token']
        if not token:
            return make_response(jsonify({"message": "A valid token missing"}), 401)        
        try:
            data = Auth.decode_auth_token(token)
            current_user = Users.find_by_id(data['user_id'])
            kwargs['user'] = current_user
           
        except:
            return make_response(jsonify({"message": "Invalid token"}), 401)

        return f(*args, **kwargs)
    return decorator


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_name', type=str, required=True, help="must have")
    parser.add_argument('password', type=str, required=True, help="must have")

    def post(self):
        data = UserLogin.parser.parse_args()
        username = data['user_name']
        password = data['password']

        return Auth.authenticate(username, password)
