from flask import Flask, session
from .routes.reports import reports_bp
from .routes.patient import patients_bp
from .routes.importfile import import_bp
from .routes.charts import charts_bp
from .config import config_session

def main():

    print("Flask API running..!")
    app = Flask(__name__)

    config_session(app)

    @app.route('/')
    def index():
        return "<p>Flask App</p>"
    
    # Register blueprints for all endpoints

    app.register_blueprint(reports_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(import_bp)
    app.register_blueprint(charts_bp)

    print("Starting the server...")
    app.run(debug=True, port=6002, host="0.0.0.0")