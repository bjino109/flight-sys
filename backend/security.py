from models import users
from hmac import compare_digest


def authenticate(username, password):
    user = users.Users.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return users.Users.find_by_id(user_id)
