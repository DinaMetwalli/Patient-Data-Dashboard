from flask import Flask, session, jsonify, request
from src.CSVParser.CSVParser import ParseCSV
from .config import *
from .routes.reports import reports_bp
from .routes.patient import patients_bp
from .routes.importfile import import_bp
from .routes.charts import charts_bp
from .routes.analyser import analyser_bp


parser = ParseCSV()
app = Flask(__name__)
app.secret_key = 'YourSecretKey'
SESSION_FILE = 'session_data.json' 

def main():
    @app.route('/')
    def index():
        session_data = load_session()
        session_data['example_key'] = 'example_value'
        save_session(session_data)
        return 'Session set'
    
    app.register_blueprint(reports_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(import_bp)
    app.register_blueprint(charts_bp)
    app.register_blueprint(analyser_bp)
    
    print("Starting the server...")
    
    app.run(debug=True, port=6002, host="0.0.0.0")
