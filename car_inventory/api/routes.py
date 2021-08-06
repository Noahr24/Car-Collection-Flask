from flask import Blueprint, json, request, jsonify
from werkzeug.wrappers import request, response
from car_inventory.helpers import token_required
from car_inventory.models import db, Car, User, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/getdata')
def getdata():
    return {'some_value': 52, 'another_value': 800}

#Create Car Endpoint
@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    make = request.json['make']
    model = request.json['model']
    color = request.json['color']
    year = request.json['year']
    price = request.json['price'+]
    user_token = current_user_token.token

    print(f'TESTER: {current_user_token.token}')

    car = Car(make, model, color, year, price, user_token=user_token)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

#Retrieve all cars
@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token, id):
    car = Car.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)

#Retreive Single Drone Endpoint
@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_drone(current_user_token, id):
    car = Car.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)


# Update a car by ID Endpoint
@api.route('/cars/<id>', methods = ['POST'])
@token_required
def update_car(current_user_token, id):
    car = Car.query.get(id)
    print(car)
    if car:
        make = request.json["make"]
        model = request.json["model"]
        color = request.json["color"]
        year = request.json["year"]
        price = request.json["price"]
        user_token = current_user_token.token
        db.session.commit()
        response = car_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That car is not here.'})


# DELETE Drone by ID
@api.route('/cars/<id>', methods= ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    if car:
        db.session.delete(car)
        db.session.commit()

        response = car_schema.dump(car)
    else:
        return jsonify({'Error': "That car is not here."})