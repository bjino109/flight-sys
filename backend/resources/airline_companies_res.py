from flask import jsonify
from flask_restful import Resource
from models import airline_companies


class Airline_Company_res(Resource):

    def get(self, name):

        user = airline_companies.Airline_Companies.find_by_name(name)
        if user:
            return user.json()
        else:
            return jsonify({'massge': 'there is not a company with thet name'})

    def delete(self, id):
        fl = airline_companies.Airline_Companies.find_by_id(id)
        if not fl:
            return jsonify({'massge': 'there is no company with thet id'})
        fl.delete_company_name()
        return jsonify({'massge': 'company  deleted!'})


class Airline_Company_by_county(Resource):

    def get(self, id):

        country = airline_companies.Airline_Companies.find_by_country_id(id)
        if country:
            return list(map(lambda x: x.json(), airline_companies.Airline_Companies.query.all()))
        else:
            return jsonify({'massge': 'there is not a company with thet country id '})


class Airline_Company_List(Resource):
    def get(self):
        return list(map(lambda x: x.json(), airline_companies.Airline_Companies.query.all()))
