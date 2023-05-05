import unittest
import requests
import random
import json


class LinearEquationHttpTestCases(unittest.TestCase):
    
    def setUp(self):
        """Initializing of server address"""
        self.address = "https://calcfree.azurewebsites.net/"

    def test_response_for_valid_equation(self):
        """Tests checks if server return status code 200 and valid answer, when equation is correct"""
        for i in range(3):
            x = random.uniform(-1000.0, 1000.0)
            if x == 0.0:
                x = 0.1
            rest = random.uniform(-1000.0, 1000.0)
            equation = str(x) +"x"
            if rest >=0:
                equation = equation + "+" + str(rest)
            else:
                equation = equation + str(rest) 
            params = {"equation": equation.replace(".", ",")}
            try:
                server_answer = requests.get(self.address + "linear-equation/", params = params)
            except ConnectionError:
                self.fail("No connection with server")                   
            self.assertTrue(server_answer.status_code == 200, msg = "Server should return status code 200")
            answer = json.loads(server_answer.text)
            self.check_for_valid_data(answer)

    def test_response_for_invalid_equation(self):
        """Tests checks if server return status code 400 and no message in answer, when equation is incorrect"""
        for i in range(3):
            x = random.uniform(-1000.0, 1000.0)
            if x == 0.0:
                x = 0.1
            rest = random.uniform(-1000.0, 1000.0)
            equation = str(x) +"x2"
            if rest >=0:
                equation = equation + "+" + str(rest)
            else:
                equation = equation + str(rest) 
            params = {"equation": equation}
            self.check_response_after_send_invalid_data(params)

            x = 0.0
            rest = random.uniform(-1000.0, 1000.0)
            equation = str(x) +"x"
            if rest >=0:
                equation = equation + "+" + str(rest)
            else:
                equation = equation + str(rest) 
            params = {"equation": equation}
            self.check_response_after_send_invalid_data(params)
            x = random.uniform(-1000.0, 1000.0)
            equation = str(x) +"x+import subprocess;"
            params = {"equation": equation.replace(".", ",")}
            self.check_response_after_send_invalid_data(params)

    def check_response_after_send_invalid_data(self, params):
        """Function checks server response for incorrect data"""
        try:
            server_answer = requests.get(self.address + "linear-equation/", params = params)
        except ConnectionError:
            self.fail("No connection with server")                   
        self.assertTrue(server_answer.status_code == 400, msg = "Server should return status code 400")
        self.assertTrue(len(server_answer.text) == 0, msg = "Length of return message should be equal")

    def check_for_valid_data(self, answer):
        """Function checks server response for correct data - if solution, hint and graph are in response"""
        self.assertTrue("solution" in answer.keys(), "Solution should be in json")
        self.assertTrue("hint" in answer.keys(), "Hint should be in json")
        self.assertTrue("graph" in answer.keys(), "Function graph should be in json")     