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

class Robot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    sight = db.Column(db.String)
    

    def __init__(self, x: int, y: int, sight):
        self.x = x
        self.y = y
        self. sight = sight

    def position(self):
        return self.x, self.y
    
    def turn_right(self):
        if self.sight == "N":
            self.sight = "E"
        elif self.sight == "E":
            self.sight = "S"
        elif self.sight == "S":
            self.sight = "W"  
        elif self.sight == "W":
            self.sight = "N" 

    def turn_left(self):
        if self.sight == "N":
            self.sight = "W"
        elif self.sight == "W":
            self.sight = "S"
        elif self.sight == "S":
            self.sight = "E"  
        elif self.sight == "E":
            self.sight = "N"   
    
    def drive(self):
        if self.sight == "N":
            self.x += 1
        elif self.sight == "E":
            self.y += 1
        elif self.sight == "S":
            self.x -= 1  
        elif self.sight == "W":
            self.y -= 1

class RobotSchema(ma.Schema):
    class Meta:
        fields = ("id", "x", "y", "sight")

robot_schema = RobotSchema()

@app.route('/robot', methods=['POST'])
def add_robot():
    x = request.json['x']
    y = request.json['y']
    sight = request.json['sight']

    new_robot = Robot(x, y, sight)

    db.session.add(new_robot)
    db.session.commit()

    return robot_schema.jsonify(new_robot)

@app.route('/robot/<id>', methods=['GET'])
def get_robot(id):
    robot = Robot.query.get(id)
    return robot_schema.jsonify(robot)



@app.route('/robot/<id>', methods=['DELETE'])
def delete_robot(id):
    robot = Robot.query.get(id)
    db.session.delete(robot)
    db.session.commit()

    return robot_schema.jsonify(robot)

@app.route('/robot/<id>/turn_right', methods=['POST'])
def turn_right(id):
    
    robot = Robot.query.get(id)
    turn_right = request.json['turn']
    robot.turn_right()
    db.session.add(robot)
    db.session.commit()

    return robot_schema.jsonify(robot)

@app.route('/robot/<id>/turn_left', methods=['POST'])
def turn_left(id):
    
    robot = Robot.query.get(id)
    turn_left = request.json['turn']
    robot.turn_left()
    db.session.add(robot)
    db.session.commit()

    return robot_schema.jsonify(robot)

@app.route('/robot/<id>/drive', methods=['POST'])
def drive(id):
    
    robot = Robot.query.get(id)
    drive = request.json['drive']
    robot.drive()
    db.session.add(robot)
    db.session.commit()

    return robot_schema.jsonify(robot)





if __name__ == '__main__':
    app.run(debug=True)