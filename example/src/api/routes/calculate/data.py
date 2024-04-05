from example.src.api.utils.Result import OK, Error, Status
from example.src.api.utils.dictify import dictify_sum
from marshmallow import Schema, fields

from example.src.calculator.calculator import Calculator

class PostSchema(Schema):
    num1 = fields.Integer(required=True)
    num2 = fields.Integer(required=True)

def post(body: dict):
    try:
        # Validate request body using Marshmallow schema
        data = PostSchema().load(body)
    except Exception as e:
        return Error(Status.BAD_REQUEST, str(e))

    try:
        # Perform calculations
        mycalc = Calculator()
        mycalc.set_num1(data["num1"])
        mycalc.set_num2(data["num2"])
        result = mycalc.add()
        if result is None:
            raise ValueError("Both numbers must be provided")
    except Exception as e:
        return Error(Status.INTERNAL_SERVER_ERROR, str(e))

    return OK(dictify_sum(mycalc))
