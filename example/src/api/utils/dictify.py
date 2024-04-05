from ...calculator.calculator import Calculator

def dictify_sum(obj: Calculator):
    return {
        "num1": obj.get_num1(),
        "num2": obj.get_num2(),
        "result": obj.add()
    }