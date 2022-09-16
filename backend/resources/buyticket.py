from models import tickets
from flask_restful import Resource, reqparse


class Buy_Ticket(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int)
    parser.add_argument('Flight_id ',
                        type=int,
                        required=True,
                        help='this format is required'
                        )
    parser.add_argument('Customer_id',
                        type=int,
                        required=True,
                        help='this format is required'
                        )

    def post(self):
        data = Buy_Ticket.parser.parse_args()
        tikcet = tickets.Tickets(
            data['id'], data['Flight_id '], data['Customer_id'])

        tikcet.save_ticket()
        return {'massge': 'ticked sold to costumer'}
