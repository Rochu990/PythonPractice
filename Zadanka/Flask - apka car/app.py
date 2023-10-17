from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.app_context().push()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_number = db.Column(db.String)
    combustion = db.Column(db.Integer)
    tank_fuel = db.Column(db.Integer)
    max_fuel = db.Column(db.Integer)
    

    def __init__(self, car_number: str, combustion: int, tank_fuel: int, max_fuel: int):
        self.car_number = car_number
        self.combustion = combustion
        self.tank_fuel = tank_fuel
        self.max_fuel = max_fuel

    def refuel(self, fuel):
        self.tank_fuel = self.tank_fuel + fuel
        if self.tank_fuel > self.max_fuel:
            print("Próbujesz zatankować za dużo")
            self.tank_fuel = self.max_fuel
        
        
    def drive(self, km):
        fuel_after_tank = self.tank_fuel
        fuel = (km / 100) * self.combustion
        self.tank_fuel = self.tank_fuel - fuel
        if self.tank_fuel < 0:
            self.tank_fuel = 0
        

class CarSchema(ma.Schema):
    class Meta:
        fields = ("id", "car_number", "combustion", "tank_fuel", "max_fuel")

car_schema = CarSchema()
cars_schema = CarSchema(many=True)


@app.route('/car', methods=['POST'])
def add_car():
    car_number = request.json['car_number']
    combustion = request.json['combustion']
    tank_fuel = request.json['tank_fuel']
    max_fuel = request.json['max_fuel']

    new_car = Car(car_number, combustion, tank_fuel, max_fuel)

    db.session.add(new_car)
    db.session.commit()

    return car_schema.jsonify(new_car)

@app.route('/car/<id>', methods=['GET'])
def get_car(id):
    car = Car.query.get(id)
    return car_schema.jsonify(car)

@app.route('/car/<id>', methods=['DELETE'])
def delete_car(id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    return car_schema.jsonify(car)

@app.route('/car/<id>/drive', methods=['POST'])
def drive(id):
    
    car = Car.query.get(id)
    km = request.json['km']
    car.drive(km)
    return car_schema.jsonify(car)

@app.route('/car/<id>/refuel', methods=['POST'])
def refuel(id):
    
    car = Car.query.get(id)
    fuel = request.json['fuel']
    car.refuel(fuel)
    return car_schema.jsonify(car)

if __name__ == '__main__':
    app.run(debug=True)