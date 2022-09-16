from flask_restful import Resource
from models import customers
from flask import jsonify


class Customers_res(Resource):
    def get(self, name):
        user = customers.Customers.find_by_name(name)
        if user:
            return user.json()
        else:
            return jsonify({'massge': 'there is not a customer with thet name'})

    def post():
        pass

    def delete(self, id):
        user = customers.Customers.find_by_id(id)
        if not user:
            return jsonify({'massge': 'there is no user with thet name'})
        user.delete_customer()
        return jsonify({'massge': 'user  deleted!'})


class customers_list(Resource):
    def get(self):
        return list(map(lambda x: x.json(), customers.Customers.query.all()))
