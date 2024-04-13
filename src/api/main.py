from flask import Flask, session, jsonify, request
import os
from src.CSVParser.CSVParser import ParseCSV
import json
parser = ParseCSV()
app = Flask(__name__)
app.secret_key = 'YourSecretKey'
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
def main():
    @app.route('/')
    def index():
        session_data = load_session()
        session_data['example_key'] = 'example_value'
        save_session(session_data)
        return 'Session set'

    @app.route('/get_session')
    def get_session():
        session_data = load_session()
        session_value = session_data.get('example_key')
        return jsonify({'session_data': session_value})

    @app.route('/upload', methods=['POST'])
    def upload_file():
        try:
            file_path = request.json.get('filePath')
            set_session_file_path(file_path)
            if not file_path:
                return jsonify({'success': False, 'message': 'No file path provided'}), 400
            if os.path.isfile(file_path):
                return jsonify({'success': True, 'message': 'File path received and file exists'}), 200
            else:
                return jsonify({'success': False, 'message': 'File does not exist at the provided path'}), 400
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 500
    @app.route("/display_charts", methods=['GET', 'POST'])
    def display_charts():
        import_name=get_session_file_path()
        print(import_name)
        try:
            parser.import_csv(import_name)

            data = {
                "encounterId": parser.data["encounterId"].tolist(),
                "end_tidal_co2": parser.data["end_tidal_co2"].tolist(),
                "feed_vol": parser.data["feed_vol"].tolist(),
                "feed_vol_adm": parser.data["feed_vol_adm"].tolist(),
                "fio2": parser.data["fio2"].tolist(),
                "fio2_ratio": parser.data["fio2_ratio"].tolist(),
                "insp_time": parser.data["insp_time"].tolist(),
                "oxygen_flow_rate": parser.data["oxygen_flow_rate"].tolist(),
                "peep": parser.data["peep"].tolist(),
                "pip": parser.data["pip"].tolist(),
                "resp_rate": parser.data["resp_rate"].tolist(),
                "sip": parser.data["sip"].tolist(),
                "tidal_vol": parser.data["tidal_vol"].tolist(),
                "tidal_vol_actual": parser.data["tidal_vol_actual"].tolist(),
                "tidal_vol_kg": parser.data["tidal_vol_kg"].tolist(),
                "tidal_vol_spon": parser.data["tidal_vol_spon"].tolist(),
                "bmi": parser.data["bmi"].tolist(),
                "referral": parser.data["referral"].tolist()
            }
            return jsonify({"success": True, "data": data})
        except Exception as e:
            return jsonify({"success": False, "message": str(e)})
    app.run(debug=True, port=6002, host="0.0.0.0")
