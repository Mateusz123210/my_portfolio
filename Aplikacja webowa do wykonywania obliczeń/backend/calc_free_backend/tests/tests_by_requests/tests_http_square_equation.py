import unittest
import requests
import random
import json


class SquareEquationHttpTestCases(unittest.TestCase):
    
    def setUp(self):
        """Initializing of server address"""
        self.address = "https://calcfree.azurewebsites.net/"

    def test_response_for_valid_equation(self):
        """Tests checks if server return status code 200 and valid answer, when equation is correct"""
        for i in range(3):
            x2 = random.uniform(-1000.0, 1000.0)
            if x2 == 0.0:
                x2 = 0.1
            x = random.uniform(-1000.0, 1000.0)
            rest = random.uniform(-1000.0, 1000.0)
            equation = str(x2) + "x^2"
            if x >=0:
                equation = equation + "+" + str(x) + "x"
            else:
                equation = equation + str(x) + "x"
            if rest >=0:
                equation = equation + "+" + str(rest)
            else:
                equation = equation + str(rest) 
            params = {"equation": equation.replace(".", ",")}
            try:
                server_answer = requests.get(self.address + "square-equation/", params = params)
            except ConnectionError:
                self.fail("No connection with server")                   
            self.assertTrue(server_answer.status_code == 200, msg = "Server should return status code 200")
            answer = json.loads(server_answer.text)
            self.check_for_valid_data(answer)

    def test_response_for_invalid_equation(self):
            """Tests checks if server return status code 400 and no message in answer, when equation is incorrect"""
            for i in range(3):
                x2 = random.uniform(-1000.0, 1000.0)
                if x2 == 0.0:
                    x2 = 0.1
                x = random.uniform(-1000.0, 1000.0)
                rest = random.uniform(-1000.0, 1000.0)
                equation = str(x2) + "x2"
                if x >=0:
                    equation = equation + "+" + str(x) + "x"
                else:
                    equation = equation + str(x) + "x"
                if rest >=0:
                    equation = equation + "+" + str(rest)
                else:
                    equation = equation + str(rest) 
                params = {"equation": equation.replace(".", ",")}
                self.check_response_after_send_invalid_data(params)

                x2 = 0.0
                x = random.uniform(-1000.0, 1000.0)
                rest = random.uniform(-1000.0, 1000.0)
                equation = str(x2) + "x2"
                if x >=0:
                    equation = equation + "+" + str(x) + "x"
                else:
                    equation = equation + str(x) + "x"
                if rest >=0:
                    equation = equation + "+" + str(rest)
                else:
                    equation = equation + str(rest) 
                params = {"equation": equation.replace(".", ",")}
                self.check_response_after_send_invalid_data(params)

                x2 = random.uniform(-1000.0, 1000.0)
                if x2 == 0.0:
                    x2 = 0.1
                x = random.uniform(-1000.0, 1000.0)
                rest = random.uniform(-1000.0, 1000.0)
                equation = str(x2) + "x2"
                if x >=0:
                    equation = equation + "+" + str(x) + "x"
                else:
                    equation = equation + str(x) + "x"
                if rest >=0:
                    equation = equation + "+" + str(rest)
                else:
                    equation = equation + str(rest) 
                equation = equation + ";import subprocess"
                params = {"equation": equation.replace(".", ",")}
                self.check_response_after_send_invalid_data(params)

    def check_response_after_send_invalid_data(self, params):
        """Function checks server response for incorrect data"""
        try:
            server_answer = requests.get(self.address + "square-equation/", params = params)
        except ConnectionError:
            self.fail("No connection with server")                   
        self.assertTrue(server_answer.status_code == 400, msg = "Server should return status code 400")
        self.assertTrue(len(server_answer.text) == 0, msg = "Length of return message should be equal")

    def check_for_valid_data(self, answer):
        """Function checks server response for correct data"""
        self.assertTrue("solution" in answer.keys(), "Solution should be in json")
        self.assertTrue("hint" in answer.keys(), "Formula should be in json")
        self.assertTrue("graph" in answer.keys(), "Function graph should be in json")     