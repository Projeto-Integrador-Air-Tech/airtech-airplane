from flask import Flask
from routes.model.model_manipulation import ModelManipulation

def run_app():
    model_app = Flask(__name__)
    ModelManipulation(model_app)
    return model_app
