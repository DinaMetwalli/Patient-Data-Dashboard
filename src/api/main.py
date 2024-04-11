from flask import Flask
from flask import  session
from .routes.importfile import import_bp
from .routes.charts import charts_bp
from .config import config_session


def main():

    print("Flask API running..!")
    app = Flask(__name__)

    config_session(app) #THIS TO MAIN.py where you connect everything

    @app.route('/')
    def index():
        return "<p>Flask App</p>"
    
    # Register blueprints for all endpoints
    app.register_blueprint(import_bp)
    app.register_blueprint(charts_bp)

    print("Starting the server...")
    app.run(debug=True, port=6002, host="0.0.0.0")