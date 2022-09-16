
from db import db


class Airline_Companies(db.Model):
    __tablename__ = 'airline_companies'

    id = db.Column(db.Integer, primary_key=True)
    Company_Name = db.Column(db.String(80), unique=True)
    User_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    user = db.relationship('Users')
    country = db.relationship('Countries')

    def __init__(self, id, Company_Name, country_id):
        self.id = id
        self.Company_Name = Company_Name
        self.country_id = country_id

    def json(self):
        return ({'id': self.id,
                 'Company_Name': self.Company_Name,
                 'user_id': self.user.user_name,
                 'contry_id': self.country.Name
                 })

    def save_company_name(self):
        db.session.add(self)
        db.session.commit()

    def delete_company_name(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, Company_Name):
        return cls.query.filter_by(Company_Name=Company_Name).first()

    @classmethod
    def find_by_country_id(cls, country_id):
        return cls.query.filter_by(country_id=country_id).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
