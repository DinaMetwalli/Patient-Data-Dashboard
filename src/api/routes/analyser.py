from flask import Blueprint, jsonify, request
import os

from src.ccu.CCU import CCU
from ..config import *
analyser_bp = Blueprint('analyser', __name__)

ccu = CCU()


@analyser_bp.route('/analyser', methods=['POST'])
def ml_algorithm():
    try:
        csv_path=get_session_file_path()

        if not csv_path:
            return jsonify({'success': False, 'message': 'No file path provided'}), 400
        print(f"Received file path: {csv_path}")

        ml = ccu.algorithm()
        data = ml.algorithm(csv_path)
        analysis_data = ml.fetch_analysis_results(data)

        return jsonify({'success': True, 'data': analysis_data})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
