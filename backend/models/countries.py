from db import db
from models.airline_companies import Airline_Companies


class Countries(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=True)
    airline_id = db.relationship('Airline_Companies')
    

    def __init__(self, id, Name):
        self.id = id
        self.Name = Name

    def json(self):
        return {
            'id': self.id,
            'name': str(self.Name)
        }

    def save_countri(self):
        db.session.add(self)
        db.session.commit()

    def delete_countri(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
