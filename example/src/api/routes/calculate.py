from flask import Blueprint, jsonify, request
from example.src.calculator.paths import MyClass

calculate = Blueprint('csv', __name__)

@calculate.route("/calculate-data", methods=["POST"])
def import_csv():
    try:
        received_data = request.json # data is sent in JSON format
        num1 = received_data.get('num1')
        num2 = received_data.get('num2')

        instance = MyClass()
        calc = instance.calculator()
        calc.set_num1(num1)
        calc.set_num2(num2)
        result = calc.add()
        data = {
            "num1": num1,
            "num2": num2,
            "result": result
        }
        
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})