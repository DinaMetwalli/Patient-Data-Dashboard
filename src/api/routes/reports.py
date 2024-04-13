from flask import Blueprint, jsonify, request
from ..config import *

from src.ccu.CCU import CCU

reports_bp = Blueprint('report', __name__)

ccu = CCU()

@reports_bp.route("/patient-report", methods=["POST"])
def patient_report():
    try:
        received_data = request.json
        csv_path=get_session_file_path()
        print(csv_path)
        patient_id = received_data.get('patient_id')
        export_name = received_data.get('export_name')

        report = ccu.reports()
        patient_rep = report.patient(patient_id, csv_path)
        patient_rep.generate_patient_report(export_name)

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    
@reports_bp.route("/average-report", methods=["POST"])
def average_report():
    try:
        received_data = request.json
        csv_path=get_session_file_path()
        print(csv_path)
        export_name = received_data.get('export_name')

        report = ccu.reports()
        avg_report = report.average(csv_path)
        avg_report.generate_report(export_name)

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})