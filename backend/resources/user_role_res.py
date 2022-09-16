
from flask_restful import Resource
from models import user_role


class User_Role_Res_List(Resource):
    def get(self):
        return list(map(lambda x: x.json(), user_role.User_Role.query.all()))
