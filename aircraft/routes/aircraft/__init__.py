from flask import Flask
from routes.aircraft.aircraft_manipulation import AircraftManipulation

def run_app():
    aircraft_app = Flask(__name__)
    AircraftManipulation(aircraft_app)
    return aircraft_app
