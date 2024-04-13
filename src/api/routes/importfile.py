from flask import Blueprint, jsonify, request
import os
from ..config import *
import_bp = Blueprint('importfile', __name__)

@import_bp.route('/upload', methods=['POST'])
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