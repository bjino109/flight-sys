from flask import jsonify
from db import db


class User_Role(db.Model):
    __tablename__ = 'user_role'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50))
    role = db.relationship('Users', lazy='dynamic')

    def __init__(self, id, role_name):
        self.id = id
        self.role_name = role_name

    def json(self):
        return {'id': self.id, 'role_name': self.role_name}
