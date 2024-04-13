# IGNORE THIS FILE
from flask import Flask, session
from flask_session import Session

def main():
    app = Flask(__name__)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config.from_object(__name__)
    Session(app)

    msg = "Hello World"

    @app.route("/set/", methods=["GET", "POST"])
    def set_session():
        value = "hi"
        session["key"] = value
        return "<h1>Ok</h1>"

    @app.route("/get/")
    def get_session():
        stored_session = session.get("key", "No session was stored")
        return f"<h3>{stored_session}</h3>"

    app.run(debug=True, host="0.0.0.0", port=6333, threaded=True)