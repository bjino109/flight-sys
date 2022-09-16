from db import db


class Tickets(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    Flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'))
    Customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    Customer = db.relationship('Customers')
    flight = db.relationship('Flights')

    def __init__(self, id, Flight_id, Customer_id):
        self.id = id
        self.Flight_id = Flight_id
        self.Customer_id = Customer_id

    def json(self):
        return{
            'id': self.id,
            'Flight_id': self.flight.id,
            'Customer_id': self.Customer.First_Name,
        }

    def save_ticket(self):
        db.session.add(self)
        db.session.commit()

    def delete_ticket(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_customer(cls, Customer_id):
        return cls.query.filter_by(Customer_id=Customer_id).first()
