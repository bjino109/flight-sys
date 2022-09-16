from flask import jsonify
from flask_restful import Resource, reqparse
from models import flights


class Flights_Create(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int)
    parser.add_argument('Airline_comp_id',
                        type=int,
                        required=True,
                        help='this format is required')
    parser.add_argument('Origen_Country_id',
                        type=int,
                        required=True,
                        help='this format is required')
    parser.add_argument('Destination_Country_id',
                        type=int,
                        required=True,
                        help='this format is required')
    parser.add_argument('Remaining_Tickets',
                        type=int,
                        required=True,
                        help='this format is required')

    def post(self):
        data = Flights_Create.parser.parse_args()

        flight = flights.Flights(data['id'], data['Airline_comp_id'], data['Origen_Country_id'],
                                 data['Destination_Country_id'], data['Remaining_Tickets'])
        flight.save_flight()
        return {'massge': 'flight crated'}

class Flight_Update(Resource):
     parser = reqparse.RequestParser()
     parser.add_argument('id', type=int)
     parser.add_argument('Airline_comp_id',
                     type=int,
                     required=True,
                     help='this format is required')
     parser.add_argument('Origen_Country_id',
                     type=int,
                     required=True,
                     help='this format is required')
     parser.add_argument('Destination_Country_id',
                     type=int,
                     required=True,
                     help='this format is required')
     parser.add_argument('Remaining_Tickets',
                     type=int,
                     required=True,
                     help='this format is required')

     def put(self,id): 
        data = Flight_Update.parser.parse_args()

        flight = flights.Flights.find_by_id(id)

        if flight:
            flight.id= data.id
            flight.Airline_comp_id=data.Airline_comp_id
            flight.Origen_Country_id = data.Origen_Country_id
            flight.Destination_Country_id = data.Destination_Country_id
            flight.Remaining_Tickets = data.Remaining_Tickets

        flight.save_flight()

        return {'flight apdate' : flight.json()} 



