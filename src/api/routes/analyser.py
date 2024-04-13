from flask import Blueprint, jsonify, request
import os

from src.ccu.CCU import CCU

analyser_bp = Blueprint('analyser', __name__)

ccu = CCU()


@analyser_bp.route('/analyser', methods=['POST'])
def ml_algorithm():
    try:
        received_data = request.json

        file_path = received_data.get('file_path')

        if not file_path:
            return jsonify({'success': False, 'message': 'No file path provided'}), 400
        print(f"Received file path: {file_path}")

        ml = ccu.algorithm()
        data = ml.algorithm(file_path)
        analysis_data = ml.fetch_analysis_results(data)

        return jsonify({'success': True, 'data': analysis_data})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
