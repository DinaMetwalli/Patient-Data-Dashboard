from flask import Flask
from .routes.reports import reports_bp
from .routes.patient import patients_bp

def main():

    print("Flask API running..!")
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "<p>Flask App</p>"
    
    # Register blueprints for all endpoints
    app.register_blueprint(reports_bp)
    app.register_blueprint(patients_bp)

    print("Starting the server...")
    app.run(debug=True, port=6002, host="0.0.0.0")