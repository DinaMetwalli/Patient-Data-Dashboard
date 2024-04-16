from flask import Blueprint, jsonify, request
import os
from ..config import *
from src.ccu.CCU import CCU

ccu = CCU()

import_bp = Blueprint('importfile', __name__)


@import_bp.route('/upload', methods=['POST'])
def upload_file():
    try:
        file_path = request.json.get('filePath')
        set_session_csv_old(file_path)
        ml = ccu.algorithm()
        analysis_data = ml.algorithm(file_path)
        parser = ccu.csv_parser()
        parser.export_csv(analysis_data)

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        result_file = os.path.join(desktop_path, "Analysed Data/Analysis_Results.csv")

        if not file_path:
            return jsonify({'success': False, 'message': 'No file path provided'}), 400
        if os.path.isfile(file_path):
            if os.path.isfile(result_file):
                set_session_file_path(result_file)
                return jsonify(
                    {'success': True, 'message': 'File path received and file exists. Data analysed successfully'}), 200
            else:
                return jsonify({'success': False, 'message': 'Error when exporting analysis results'}), 400
        else:
            return jsonify({'success': False, 'message': 'File does not exist at the provided path'}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
