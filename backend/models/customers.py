
from db import db


class Customers(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(80))
    Last_Name = db.Column(db.String(80))
    Address = db.Column(db.String(80))
    Phone_No = db.Column(db.String(80), unique=True)
    Credit_Card_No = db.Column(db.String(80), unique=True)
    ticket_id = db.relationship('Tickets')
    User_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')

    def __init__(self, id, First_Name, Last_Name, Address, Phone_No, Credit_Card_No, User_id):
        self.id = id
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Address = Address
        self.Phone_No = Phone_No
        self.Credit_Card_No = Credit_Card_No
        self.User_id = User_id

    def json(self):
        return({'id': self.id,
                'first_name': self.First_Name,
                'last_name': self.Last_Name,
                'address': self.Address,
                 'Phone_No': self.Phone_No,
                'Credit_Card_No': self.Credit_Card_No,
                'phone_num': self.Phone_No,
                'User_id ': self.user.id,
                })

    def save_customer(self):
        db.session.add(self)
        db.session.commit()

    def delete_customer(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, First_Name):
        return cls.query.filter_by(First_Name=First_Name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
