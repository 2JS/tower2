from flask import Flask
from flask_restful import Resource, Api, reqparse
import tower

tower = tower.Tower()

class Heater(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('value', type=float)
    args = parser.parse_args()
    print(args)
    temp = args['value']
    
    tower.heater.setTemperature(float(temp))
    
    return {}, 200
  
  def get(self):
    temp = tower.heater.getTemperature()
    return {"value": temp}, 200

class Extruder(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('value')
    args = parser.parse_args()

    speed = args['value']
    tower.extruder.setSpeed(float(speed))
    return {}, 200

  def get(self):
    return {"value": tower.extruder.getSpeed()}, 200

class Fiber(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('value')
    args = parser.parse_args()

    speed = args['value']
    tower.fiber.setSpeed(float(speed))
    return {}, 200
  
  def get(self):
    return {"value": tower.fiber.getSpeed()}, 200
