from flask import Blueprint, jsonify, request
import os

from src.ccu.CCU import CCU

auth_bp = Blueprint('authentication', __name__)

ccu = CCU()

@auth_bp.route('/auth-entry', methods=['POST'])
def auth_entry():
    try:
        received_data = request.json

        password = received_data.get('entry_password')
        print(password)

        ccu.entry_password(password)

        return jsonify({"success": True, "message": "Entry Passkey Validated!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    
@auth_bp.route('/auth-import', methods=['POST'])
def auth_import():
    try:
        received_data = request.json

        password = received_data.get('import_password')

        ccu.import_password(password)
        
        return jsonify({"success": True, "message": "Import passkey validated!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    
@auth_bp.route('/auth-export', methods=['POST'])
def auth_export():
    try:
        received_data = request.json

        password = received_data.get('export_password')

        ccu.export_password(password)
        
        return jsonify({"success": True, "message": "Export passkey validated!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    
@auth_bp.route('/setup', methods=['POST'])
def auth_setup():
    try:
        received_data = request.json

        entry_pass = received_data.get('entry_pass')
        import_pass = received_data.get('import_pass')
        export_pass = received_data.get('export_pass')

        ccu.setup_passwords(entry_pass, import_pass, export_pass)

        return jsonify({"success": True, "message": "Passwords set successfully."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    