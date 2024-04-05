from flask import Flask
from .api.utils.FSrouter import FSRouter

def main():

    print("Flask API running..!")
    app: Flask = Flask("Feeding Dashboard")

    router = FSRouter(app)
    router.load_dir("example\\src\\api\\routes")

    @app.route('/')
    
    def index():
        return "<p>Testing</p>"
    
    print("Starting the server...")
    app.run(debug=True, port=6002, host="0.0.0.0")
