class Calculator:
    def __init__(self):
        self.num1 = None
        self.num2 = None

    def set_num1(self, number):
        self.num1 = number

    def set_num2(self, number):
        self.num2 = number

    def get_num1(self):
        return self.num1

    def get_num2(self):
        return self.num2

    def minus(self):
        return self.num1 - self.num2