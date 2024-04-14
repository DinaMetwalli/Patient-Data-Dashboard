from flask import Blueprint, jsonify, request
from src.CSVParser.CSVParser import ParseCSV
from ..config import *
referal_bp = Blueprint('referal', __name__)
parser = ParseCSV()
@referal_bp.route("/referal", methods=['POST', 'GET'])
def referal():
        without_algorithm=get_session_csv_old()
        print(without_algorithm)
        try:
            parser.import_csv(without_algorithm)

            data = {
                "referral": parser.data["referral"].tolist()
            }
            return jsonify({"success": True, "data": data})
        except Exception as e:
            return jsonify({"success": False, "message": str(e)})