import unittest
import requests
import random
import json


class BubbleSortHttpTestCases(unittest.TestCase):
    
    def setUp(self):
        """Initializing of server address"""
        self.address = "https://calcfree.azurewebsites.net/"

    def test_response_for_valid_equation_sorting_ascending(self):
        """Tests checks if server return status code 200 and valid answer, when equation is correct"""
        for i in range(3):
            number_of_numbers = random.randint(2,30)
            numbers = ""
            for i in range(number_of_numbers):
                numbers = numbers + str(random.uniform(-1000.0, 1000.0)).replace(".", ",") + ";"
            numbers = numbers[:-1]
            params = {"numbers": numbers, "ascending": "yes"}
            try:
                server_answer = requests.get(self.address + "bubble-sort/", params = params)
            except ConnectionError:
                self.fail("No connection with server")                   
            self.assertTrue(server_answer.status_code == 200, msg = "Server should return status code 200")
            answer = json.loads(server_answer.text)
            self.check_for_valid_data(answer)

    def test_response_for_invalid_equation(self):
            """Tests checks if server return status code 400 and no message in answer, when equation is incorrect"""
            for i in range(3):
                numbers = ""
                number_of_numbers = random.randint(2,100)
                for i in range(number_of_numbers):
                    numbers = numbers + "s;"                
                params = {"numbers": numbers}
                self.check_response_after_send_invalid_data(params)

                numbers = ""
                number_of_numbers = random.randint(2,100)
                for i in range(number_of_numbers):
                    numbers = numbers + str(random.uniform(-1000.0, 1000.0)).replace(".", ",") + ";"
                params = {"numbers": numbers}
                self.check_response_after_send_invalid_data(params)

                numbers = ""
                number_of_numbers = random.randint(2,100)
                for i in range(number_of_numbers):
                    numbers = numbers + str(random.uniform(-1000.0, 1000.0)).replace(".", ",") + ";"
                numbers = numbers + ";print(\"server hacked\");"
                params = {"numbers": numbers}
                self.check_response_after_send_invalid_data(params)

    def check_response_after_send_invalid_data(self, params):
        """Function checks server response for incorrect data"""
        try:
            server_answer = requests.get(self.address + "bubble-sort/", params = params)
        except ConnectionError:
            self.fail("No connection with server")                   
        self.assertTrue(server_answer.status_code == 400, msg = "Server should return status code 400")
        self.assertTrue(len(server_answer.text) == 0, msg = "Length of return message should be equal")

    def check_for_valid_data(self, answer):
        """Function checks server response for correct data"""
        self.assertTrue("solution" in answer.keys(), "Solution should be in json")
        self.assertTrue("hint" in answer.keys(), "Formula should be in json")  