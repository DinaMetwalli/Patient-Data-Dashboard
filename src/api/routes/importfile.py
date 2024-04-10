from flask import Blueprint, jsonify, request
import os
import_bp = Blueprint('importfile', __name__)

@import_bp.route('/upload', methods=['POST'])
def upload_file():
    file_path = request.json.get('filePath')

    if not file_path:
        return jsonify({'success': False, 'message': 'No file path provided'}), 400
    print(f"Received file path: {file_path}")
    if os.path.isfile(file_path):
        return jsonify({'success': True, 'message': 'File path received and file exists'}), 200
    else:
        return jsonify({'success': False, 'message': 'File does not exist at the provided path'}), 400