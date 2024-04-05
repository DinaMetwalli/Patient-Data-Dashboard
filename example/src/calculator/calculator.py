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

    def add(self):
        # plugin for flask or inbuilt flask thing for authentication, this could be tokens or sessions.
        # basically, you need to add some sort of sessions for the login, the person doesn't just login and your flask
        # app sends the password that it fetched from the electron to the API endpoint and then it just compares it to what
        # it expects and says ok and then anyone with the url (ex: localhost:6002\calculate\data not \login) (although you 
        # proved your point that this isnt possible) can access the dashboard. you need to add authentication or sessions.
        return self.num1 + self.num2