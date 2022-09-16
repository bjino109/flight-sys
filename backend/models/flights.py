from datetime import datetime, timedelta
from db import db


class Flights(db.Model):
    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key=True)
    Airline_comp_id = db.Column(
        db.Integer, db.ForeignKey('airline_companies.id'))
    Airline_comp = db.relationship('Airline_Companies')
    Origen_Country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    Origen_Country = db.relationship(
        "Countries", foreign_keys=[Origen_Country_id])
    Destination_Country_id = db.Column(
        db.Integer, db.ForeignKey('countries.id'))
    Destination_Country = db.relationship(
        "Countries", foreign_keys=[Destination_Country_id])
    departure_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now()-timedelta(hours=2))
    landing_time = db.Column(db.DateTime, nullable=False,
                             default=datetime.now()+timedelta(hours=3))
    Remaining_Tickets = db.Column(db.Integer)

    def __init__(self, id, Airline_comp_id, Origen_Country_id, Destination_Country_id, Remaining_Tickets):
        self.id = id
        self.Airline_comp_id = Airline_comp_id
        self.Origen_Country_id = Origen_Country_id
        self.Destination_Country_id = Destination_Country_id
        # self.departure_time = departure_time
        # self.landing_time = landing_time
        self.Remaining_Tickets = Remaining_Tickets

    def json(self):
        return ({'id': self.id,
                 'company_name': self.Airline_comp.Company_Name,
                 'Origen': self.Origen_Country.Name,
                 'Destination': self.Destination_Country.Name,
                 'departure_time': str(self.departure_time),
                 'landing_time': str(self.landing_time),
                 'Remaining_Tickets': self.Remaining_Tickets
                 })

    def save_flight(self):
        db.session.add(self)
        db.session.commit()

    def delete_flight(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_Flights_By_Origin_CountryId(cls, Origen_Country_id):
        return cls.query.filter_by(Origen_Country_id=Origen_Country_id).first()

    @classmethod
    def find_Flights_By_Destination_Country_id(cls, Destination_Country_id):
        return cls.query.filter_by(Destination_Country_id=Destination_Country_id).first()
