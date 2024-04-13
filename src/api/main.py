from flask import Flask, jsonify, request, session, make_response
from flask_session import Session
from flask_cors import CORS, cross_origin
from .routes.charts import charts_bp
# import redis

from src.ccu.CCU import CCU

import os

def main():

    print("Flask API running..!")

    app = Flask(__name__)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config.from_object(__name__)
    Session(app)
    CORS(app)

    ccu = CCU()
    parser = ccu.csv_parser()

    @app.route("/upload/", methods=["GET", "POST"])
    @cross_origin(supports_credentials=True)
    def upload_file():
        file_path = request.json.get('filePath')

        if not file_path:
            return jsonify({'success': False, 'message': 'No file path provided'}), 400

        print(f"Received file path: {file_path}")
        if os.path.isfile(file_path):
            session['path'] = 'Data.csv'
            print(session['path'])

            return jsonify({'success': True, 'message': 'File path received and file exists'}), 200
        else:
            return jsonify({'success': False, 'message': 'File does not exist at the provided path'}), 400
        
    @app.route("/display_charts/", methods=["GET", "POST"])
    @cross_origin(supports_credentials=True)
    def display_charts():
        try:
            # if not session.has_session:  # Check if a session exists
            #     return jsonify({'success': False, 'message': 'No session found'}), 401
            import_name = session.get('path', 'No session was stored')
            print(import_name, "!!!")

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

    print("Starting the server...")
    app.run(debug=True, port=6002, host="0.0.0.0", threaded=True)