import os
import json
SESSION_FILE = 'session_data.json' 
def load_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_session(session_data):
    with open(SESSION_FILE, 'w') as f:
        json.dump(session_data, f)

def get_session_file_path():
    session_data = load_session()
    return session_data.get('csv_file')

def set_session_file_path(file_path):
    session_data = load_session()
    session_data['csv_file'] = file_path
    save_session(session_data)