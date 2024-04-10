from flask import Flask
from .routes.calculate import calculate

def main():

    print("Flask API running..!")
    app = Flask(__name__)
    
    # Register blueprints for all endpoints
    app.register_blueprint(calculate)

    print("Starting the server...")
    app.run(debug=True, port=6002, host="0.0.0.0")
