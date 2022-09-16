
from db import db


class Administrators(db.Model):
    __tablename__ = 'administrators'

    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(80))
    Last_Name = db.Column(db.String(80))
    User_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')

    def __init__(self, id, First_Name, Last_Name, User_id):
        self.id = id
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.User_id = User_id

    def json(self):
        return {
            'id': self.id,
            'First_Name': self.First_Name,
            'Last_Name': self.Last_Name,
            'user_id': self.User_id
        }

    def save_administrators(self):
        db.session.add(self)
        db.session.commit()

    def delete_administrators(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_first_Name(cls, First_Name):
        return cls.query.filter_by(First_Name=First_Name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
