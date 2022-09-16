
from flask_restful import Resource, reqparse


from models import users


class User_Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int)
    parser.add_argument('user_name',
                        type=str,
                        required=True,
                        help='this format is required'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='this format is required'
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='this format is required'
                        )
    parser.add_argument('role_id',
                        type=int,
                        required=True,
                        help='this format is required'
                        )

   
    def post(self):
        data = User_Register.parser.parse_args()
        if users.Users.find_by_username(data['user_name']):
            return {'massge': "user with thet name is allredy existes"}

        user = users.Users(data['id'], data['user_name'],
                           data['password'], data['email'], data['role_id'])
        user.save_user()
        return {'massge':  "user crated"}


class User_Res_UPdate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int)
    parser.add_argument('user_name',
                        type=str,
                        required=True,
                        help='this format is required'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='this format is required'
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='this format is required'
                        )
    parser.add_argument('role_id',
                        type=int,
                        required=True,
                        help='this format is required'
                        )

    def put(self, id):
        data = User_Res_UPdate.parser.parse_args()

        user = users.Users.find_by_id(id)

        if user:
            user.id = data.id
            user.user_name = data.user_name
            user.password = data.password
            user.email = data.email
            user.role_id = data.role_id

        user.save_user()

        return {'user Apdate ':     user.json()}
