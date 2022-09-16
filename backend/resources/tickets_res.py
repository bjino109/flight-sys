from flask_restful import Resource
from models import tickets
from flask import jsonify
from flask_restful import Resource, reqparse


class Tickets_Res(Resource):
    def get(self, id):
        tic = tickets.Tickets.find_by_id(id)
        if tic:
            return tic.json()
        else:
            return jsonify({'massge': 'cant find ticket with thet id '})

    def delete(self, id):
        ticket = tickets.Tickets.find_by_id(id)
        if not ticket:
            return jsonify({'massge': 'there is no ticket with thet id'})
        ticket.delete_ticket()
        return jsonify({'massge': 'ticket remove'})


class Flight_by_costomer(Resource):

    def get(self, id):
        costumer = tickets.Tickets.find_by_customer(id)
        if costumer:
            return costumer.json()
        else:
            return jsonify({'massge': 'cant find costomer with thet data '})



















