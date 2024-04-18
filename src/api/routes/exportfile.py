from flask import Blueprint, jsonify, request
import os
from ..config import *
from src.ccu.CCU import CCU

ccu = CCU()

export_bp = Blueprint('exportfile', __name__)


@export_bp.route('/export', methods=['POST'])
def export_file():
    try:
        results_path = get_session_file_path()
        parser = ccu.csv_parser()
        analysis_results = parser.import_csv(results_path)
        parser.export_csv(analysis_results, "Analysis_Results.csv")

        return jsonify({'success': True, 'message': 'CSV file exported to Analysis Data directory'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
