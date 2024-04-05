from flask import Flask, request
from example.src.api.routes.calculate.data import post

def main():

    print("Flask API running..!")
    app: Flask = Flask("Feeding Dashboard")

    @app.route('/')
    def index():
        return "<p>Testing</p>"
    
    @app.route('/calculate/data', methods=['POST'])
    def calculate():
        request_data = request.json
        response, status_code = post(request_data)
        return response, status_code
    
    print("Starting the server...")
    app.run(debug=True, port=6002, host="0.0.0.0")
