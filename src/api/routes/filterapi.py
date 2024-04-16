from flask import Blueprint, jsonify, request
from src.ccu.CCU import CCU

ccu = CCU()

filter_bp = Blueprint('filter', __name__)


@filter_bp.route('/filter-by-bmi', methods=['POST'])
def filter_by_bmi():
    try:
        bmi = request.json.get('bmi')
        filtered_data = ccu.filter_by_bmi(bmi)  # Call your backend method to filter by BMI
        return jsonify({'success': True, 'data': filtered_data}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@filter_bp.route('/filter-by-referral', methods=['POST'])
def filter_by_referral():
    try:
        referral = request.json.get('referral')
        filtered_data = ccu.filter_by_referral(referral)  # Call your backend method to filter by referral status
        return jsonify({'success': True, 'data': filtered_data}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
