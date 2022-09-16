from db import db
from models.user_role import User_Role


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(250), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'))
    role = db.relationship('User_Role')
    custumer = db.relationship('Customers')

    def __init__(self, id, user_name, password, email, role_id):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.email = email
        self.role_id = role_id

    def json(self):
        return {'id': self.id,
                'username': self.user_name,
                'password': self.password,
                'email': self.email,
                'role_name': self.role.role_name}

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user_name):
        return cls.query.filter_by(user_name=user_name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
