from flask import jsonify
from flask_restful import Resource
from models import countries


class Countries_res(Resource):
    def get(self, id):
        countri = countries.Countries.find_by_id(id)
        if countri:
            return countri.json()
        else:
            return jsonify({'massge': 'there isnt country with then name'})

    def post():
        pass

    def delete(self, id):
        countri = countries.Countries.find_by_id(id)
        if not countri:
            return jsonify({'massge': 'there is no countri with thet name'})
        countri.delete_countri()
        return jsonify({'massge': 'country  deleted!'})


class Countries_res_List(Resource):
    def get(self):
        return list(map(lambda x: x.json(), countries.Countries.query.all()))
