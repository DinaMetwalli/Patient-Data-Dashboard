from flask import Blueprint, jsonify, request
from src.ccu.CCU import CCU
from ..config import *

ccu = CCU()

filter_bp = Blueprint('filter', __name__)


@filter_bp.route('/filter-by-bmi', methods=['POST'])
def filter_by_bmi():
    try:
        bmi = request.json.get('bmi')
        print("recieved bmi: ", bmi)

        csv_file = get_session_file_path()

        filters = ccu.filter()
        filtered_data = filters.filter_by_bmi(bmi, csv_file)
        return jsonify({'success': True, 'data': filtered_data}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@filter_bp.route('/filter-by-referral', methods=['POST'])
def filter_by_referral():
    try:
        referral = request.json.get('referral')
        print(referral)

        csv_file = get_session_file_path()

        filters = ccu.filter()
        filtered_data = filters.filter_by_referral(referral, csv_file)
        for i in range(25):
            print(filtered_data[-i])
        
        return jsonify({'success': True, 'data': filtered_data}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
