from flask import session

from flask_session import Session

def config_session(app):
    # Configure session to use filesystem (or any other desired configuration)
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)