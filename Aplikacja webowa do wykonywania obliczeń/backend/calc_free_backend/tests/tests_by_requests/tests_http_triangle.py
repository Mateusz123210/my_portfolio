import unittest
import requests
import random
import json


class TriangleHttpTestCases(unittest.TestCase):
    
    def setUp(self):
        """Initializing of server address"""
        self.address = "https://calcfree.azurewebsites.net/"
    
    def test_valid_three_sides(self):
        """Test checks if server returns valid response for correct data. Lenghts of
        three sides are given"""
        for i in range(3):
            a = random.uniform(0.1, 1000.0)
            b = random.uniform(0.1, 1000.0)
            c = (a**2 + b**2)**(1 / 2.0)
            params = {"firstSide": str(a).replace(".", ","), "secondSide": str(b).replace(".", ","),
                "hypotenuse": str(c).replace(".", ",")}
            try:
                server_answer = requests.get(self.address + "triangle/", params = params)
            except ConnectionError:
                self.fail("No connection with server")                   
        self.assertTrue(server_answer.status_code == 200, msg = "Server should return status code 200")
        answer = json.loads(server_answer.text)
        self.check_for_valid_data(answer)
    
    def test_valid_without_a(self):
        """Test checks if server returns valid response for correct data. Lenghts of
        b and c are given"""
        for i in range(3):
            b = random.uniform(0.1, 1000.0)
            c = random.uniform(b+0.001, 1000.12)
            params = {"secondSide": str(b).replace(".", ","), "hypotenuse": str(c).replace(".", ",")}
            try:
                server_answer = requests.get(self.address + "triangle/", params = params)
            except ConnectionError:
                self.fail("No connection with server")                   
        self.assertTrue(server_answer.status_code == 200, msg = "Server should return status code 200")
        answer = json.loads(server_answer.text)
        self.check_for_valid_data(answer)
        self.assertTrue("firstSide" in answer.keys(), "Length of a should be in json")
    
    def test_valid_without_b(self):
        """Test checks if server returns valid response for correct data. Lenghts of
        a and c are given"""
        for i in range(3):
            a = random.uniform(0.1, 1000.0)
            c = random.uniform(a+0.001, 1000.12)
            params = {"firstSide": str(a).replace(".", ","), "hypotenuse": str(c).replace(".", ",")}
            try:
                server_answer = requests.get(self.address + "triangle/", params = params)
            except ConnectionError:
                self.fail("No connection with server")                   
        self.assertTrue(server_answer.status_code == 200, msg = "Server should return status code 200")
        answer = json.loads(server_answer.text)
        self.check_for_valid_data(answer)
        self.assertTrue("secondSide" in answer.keys(), "Length of a should be in json")
    
    def test_valid_without_c(self):
        """Test checks if server returns valid response for correct data. Lenghts of
        a and b are given"""
        for i in range(3):
            a = random.uniform(0.1, 1000.0)
            b = random.uniform(0.1, 1000.0)
            params = {"firstSide": str(a).replace(".", ","), "secondSide": str(b).replace(".", ",")}
            try:
                server_answer = requests.get(self.address + "triangle/", params = params)
            except ConnectionError:
                self.fail("No connection with server")                   
        self.assertTrue(server_answer.status_code == 200, msg = "Server should return status code 200")
        answer = json.loads(server_answer.text)
        self.check_for_valid_data(answer)
        self.assertTrue("hypotenuse" in answer.keys(), "Length of a should be in json")

    def test_invalid_options(self):
        """Test contains some different cases and checks if \
             server returns status 400 for invalid data"""
        a = random.uniform(0.1, 1000.0)
        b = random.uniform(0.1, 1000.0)
        c = (a**2 + b**2)**(1 / 2.0) + 1
        params = {"firstSide": str(a).replace(".", ","), "secondSide": str(b).replace(".", ","), "hypotenuse": str(c).replace(".", ",")}
        self.send_request_and_check_invalid_sides_lenghts(params)

        a = random.uniform(0.1, 1000.0)
        b = random.uniform(0.1, 1000.0)
        c = b
        params = {"firstSide": str(a).replace(".", ","), "secondSide": str(b).replace(".", ","), "hypotenuse": str(c).replace(".", ",")}
        self.send_request_and_check_invalid_sides_lenghts(params)

        a = random.uniform(0.1, 1000.0)
        b = random.uniform(0.1, 1000.0)
        c = (a+b)/2
        params = {"firstSide": str(a).replace(".", ","), "secondSide": str(b).replace(".", ","), "hypotenuse": str(c).replace(".", ",")}
        self.send_request_and_check_invalid_sides_lenghts(params)

        a = random.uniform(-1000.0, -0.1)
        b = random.uniform(-1000.0, -0.1)
        c = (a**2 + b**2)**(1 / 2.0)
        params = {"firstSide": str(a).replace(".", ","), "secondSide": str(b).replace(".", ","), "hypotenuse": str(c).replace(".", ",")}
        self.send_request_and_check_invalid_sides_lenghts(params)

        a = "a"
        b = random.uniform(0.1, 1000.0)
        c = random.uniform(b + 0.1, 1000.4)
        params = {"firstSide": str(a).replace(".", ","), "secondSide": str(b).replace(".", ","), "hypotenuse": str(c).replace(".", ",")}
        self.send_request_and_check(params)

        a = random.uniform(0.1, 1000.0)
        b = "b"
        c = random.uniform(a + 0.1, 1000.4)
        params = {"firstSide": str(a).replace(".", ","), "secondSide": str(b).replace(".", ","), "hypotenuse": str(c).replace(".", ",")}
        self.send_request_and_check(params)

        a = random.uniform(0.1, 1000.0)
        b = random.uniform(0.1, 1000.0)
        c = "c"
        params = {"firstSide": str(a).replace(".", ","), "secondSide": str(b).replace(".", ","), "hypotenuse": str(c).replace(".", ",")}
        self.send_request_and_check(params)


    def check_for_valid_data(self, answer):
        """Function checks server response for correct data"""
        self.assertTrue(type(answer) == dict, "Answer should be valid json")
        self.assertTrue("hint" in answer.keys(), "Hint should be in json")
        self.assertTrue("sinL" in answer.keys(), "Sine alfa should be in json")
        self.assertTrue("cosL" in answer.keys(), "Cosine alfa should be in json")
        self.assertTrue("tgL" in answer.keys(), "Tangent alfa should be in json")
        self.assertTrue("ctgL" in answer.keys(), "Cotangent alfa should be in json")        

    def send_request_and_check(self, params):
        """Functions check if server returns valid response for incorrect data"""
        try:
            server_answer = requests.get(self.address + "triangle/", params = params)
        except ConnectionError:
            self.fail("No connection with server")
        self.assertTrue(server_answer.status_code == 400, msg = "Server should return status code 400")
        self.assertTrue(len(server_answer.text) == 0, "Answer text should be empty")

    def send_request_and_check_invalid_sides_lenghts(self, params):
        """Functions check if server returns error and status code is 200, when lenghts of 
        sides are incorrect"""
        try:
            server_answer = requests.get(self.address + "triangle/", params = params)
        except ConnectionError:
            self.fail("No connection with server")
        self.assertTrue(server_answer.status_code == 200, msg = "Server should return status code 200")
        self.assertTrue(len(server_answer.text) > 0, "Answer text should not be empty")
        answer = json.loads(server_answer.text)
        self.assertTrue(type(answer) == dict, "Answer should be valid json")
        self.assertTrue("error" in answer.keys(), "Error should be in json")
        self.assertTrue(len(answer) == 1, "In json should be only one key")