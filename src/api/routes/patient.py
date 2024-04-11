from flask import Blueprint, jsonify, request

from src.ccu.CCU import CCU

patients_bp = Blueprint('patient', __name__)

ccu = CCU()

@patients_bp.route("/patient", methods=["POST"])
def patient_data():
    try:
        received_data = request.json

        patient_id = received_data.get('patient_id')
        csv_path = received_data.get('csv_path') # could change/remove according to sessions

        patient = ccu.patients(csv_path)
        data = patient.fetch_patient_data(patient_id)
        patient_data = {}

        for key in data:
            patient_data[key] = data[key][0]
        

        return jsonify({"success": True, "data": patient_data})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})