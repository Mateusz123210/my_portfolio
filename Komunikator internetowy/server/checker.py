import json


class Checker:

    def __init__(self):
        self.start_curly_braces_number = 0
        self.stop_curly_braces_number = 0

    def check(self, string):

        if type(string) != str:
            return None

        if len(string) <= 2:
            return None

        if string[0] != '{':
            return None

        if string[-1] != '}':
            return None

        response = None
        try:
            response = json.loads(string)
        except ValueError:
            return None
        return response




