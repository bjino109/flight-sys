from pickle import FALSE
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from db import db
from models import users, administrators, airline_companies, countries, customers, tickets, flights
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS
from security import authenticate, identity


from resources.customers_res import Customers_res, customers_list
from resources.flights_res import Flights_list, Flights_res
from resources.user_res import User_res, User_list
from resources.admin_res import Admin_res, Admin_list
from resources.user_register import User_Register, User_Res_UPdate
from resources.airline_companies_res import Airline_Company_res, Airline_Company_by_county, Airline_Company_List
from resources.flights_res import Flights_res, Flights_list, Flights_By_Origin_CountryId, Flights_By_Destination_Country_id
from resources.flight_create import Flights_Create, Flight_Update
from resources.tickets_res import Tickets_Res, Flight_by_costomer
from resources.buyticket import Buy_Ticket
from resources.countries_res import Countries_res, Countries_res_List
from resources.userApi import UserLogin


app = Flask(__name__)
api = Api(app)
jwt = JWT(app, authenticate, identity)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api.add_resource(User_list, '/users')
api.add_resource(User_res, '/user/<name>')
api.add_resource(customers_list, '/customers')
api.add_resource(Customers_res, '/customer/<id>')
api.add_resource(Admin_list, '/admins')
api.add_resource(Admin_res, '/admin/<id>')
api.add_resource(Airline_Company_res, '/company/<id>')
api.add_resource(Airline_Company_by_county, '/companybyid/<id>')
api.add_resource(Airline_Company_List, '/companis')
api.add_resource(Countries_res_List, '/countries')
api.add_resource(Countries_res, '/country/<id>')
api.add_resource(User_Register, '/register')
api.add_resource(User_Res_UPdate, '/update/<id>')
api.add_resource(Flights_list, '/flights/')
api.add_resource(Flights_Create, '/addflight/')
api.add_resource(Flight_Update, '/updateflight/<id>')
api.add_resource(Flights_res, '/flight/<id>')
api.add_resource(Flight_by_costomer, '/filght_by_costumer/<id>')
api.add_resource(Flights_By_Origin_CountryId, '/flightsbyorigin/<id>')
api.add_resource(Flights_By_Destination_Country_id, '/flightsbydes/<id>')
api.add_resource(Tickets_Res, '/ticket/<id>')
api.add_resource(Buy_Ticket, '/buyticket')
api.add_resource(UserLogin, '/login')


# @app.route('/flights/')
# def ins_flight():'
#     fl1 = flights.Flights(1, 1, 4, 6)
#     db.session.add(fl1)
#     db.session.commit()
#     return jsonify({'massge': 'flight created'})


@app.before_first_request
def create_table():
    db.create_all()

db.init_app(app)
if __name__ == '__main__':
    app.run(port=5000, debug=FALSE)
