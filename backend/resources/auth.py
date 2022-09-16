import jwt
import datetime
from models.users import Users
from hmac import compare_digest
from .import common


class Auth():
    @staticmethod
    def encode_auth_token(user):
        try:

            payload = {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1, hours=0, minutes=0, seconds=20),
                "iat": datetime.datetime.utcnow(),
                "user_id": user.id,
                "email": user.email,

            }

            signature = jwt.encode(payload, 'jbs', algorithm="HS256")
            return signature
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, 'jbs', optios={
                                 'verify_exp': True})
            if payload:
                return payload
            else:
                raise jwt.InvalidTokenError

        except jwt.ExpiredSignatureError:
            return 'Token Expired'
        except jwt.InvalidTokenError:
            return 'Invalid Token'

    @classmethod
    def authenticate(cls, username, password):
        user = Users.find_by_username(username)
        if user and compare_digest(user.password, password):
            token = cls.encode_auth_token(user)
            return {"access_token": token.decode('utf-8')}, 200
        else:
            return {"desciption": "Invalid credentials", "status_code": 401, "error": "Bad Request"}, 401

    @classmethod
    def identity(cls, token):
        try:
            if not token or token['headers']['typ'] != 'JWT':
                return common.falseReturn('', "Please pass correct auth token")

            payload = cls.decode_auth_token(token)
            user = Users.find_by_id(payload['payload']['user_id'])
            if user is None:
                return common.falseReturn('', "User information not found")
                # return {"desciption": "User information not found"
                #     , "status_code" : 401
                #     ,"error": "Bad Request"}, 401
            else:
                return common.trueReturn(user.id, "request suceeseded")
        except jwt.ExpiredSignatureError:
            return 'Token Expired'
        except jwt.InvalidTokenError:
            return 'Invalid Token'
