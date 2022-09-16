from flask import jsonify
from flask_restful import Resource, reqparse
from models import flights


class Flights_res(Resource):

    def get(self, id):
        f_id = flights.Flights.find_by_id(id)
        if f_id:
            return f_id.json()
        else:
            return jsonify({'massge': 'flight not found'})

    def delete(self, id):
        fl = flights.Flights.find_by_id(id)
        if not fl:
            return jsonify({'massge': 'there is no flight with thet id'})
        fl.delete_flight()
        return jsonify({'massge': 'flight  deleted!'})


class Flights_By_Origin_CountryId (Resource):
    def get(self, id):
        flight = flights.Flights.find_Flights_By_Origin_CountryId(id)
        if flight:
            return flight.json()
        else:
            return jsonify({'massge': 'cant find flight with thet  Origin_CountryId'})


class Flights_By_Destination_Country_id (Resource):
    def get(self, id):
        flight = flights.Flights.find_Flights_By_Destination_Country_id(id)
        if flight:
            return flight.json()
        else:
            return jsonify({'massge': 'cant find flight with thet  Destination_Country_id'})


class Flights_list(Resource):
    def get(self):
        return list(map(lambda x: x.json(), flights.Flights.query.all()))
