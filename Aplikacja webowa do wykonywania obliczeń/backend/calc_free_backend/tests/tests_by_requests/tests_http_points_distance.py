import unittest
import requests
import random
import json


class PointsDistanceHttpTestCases(unittest.TestCase):
    
    def setUp(self):
        """Initializing of server address"""
        self.address = "https://calcfree.azurewebsites.net/"

    def test_correct_numbers(self):
        """Checking server answer, when params are correct"""
        for i in range(3):
            x1 = random.uniform(-1000.0, 1000.0)
            y1 = random.uniform(-1000.0, 1000.0)
            x2 = random.uniform(-1000.0, 1000.0)
            y2 = random.uniform(-1000.0, 1000.0)
            params = {"firstPoint": str(x1).replace(".", ",") + ";" + str(y1).replace(".", ","),
             "secondPoint": str(x2).replace(".", ",") + ";" + str(y2).replace(".", ",")}
            try:
                server_answer = requests.get(self.address + "points-distance/", params = params)
            except ConnectionError:
                self.fail("No connection with server")
            self.assertTrue(server_answer.status_code == 200, msg = "Server should return status code 200")
            answer = json.loads(server_answer.text)
            self.assertTrue(type(answer) == dict, "Answer should be valid json")
            self.assertTrue("solution" in answer.keys(), "Solution should be in json")
            self.assertTrue("hint" in answer.keys(), "Hint should be in json")
            self.assertTrue("graph" in answer.keys(), "Graph should be in json")

    def test_incorrect_numbers(self):
        """Checking server answer, when params are incorrect"""
        x1 = random.uniform(-1000.0, 1000.0)
        y1 = random.uniform(-1000.0, 1000.0)
        x2 = random.uniform(-1000.0, 1000.0)
        y2 = random.uniform(-1000.0, 1000.0)
        params = {"firstPoint": str(x1).replace(".", ",") + ";" + str(y1).replace(".", ","), 
        "secondPoint": str(x2).replace(".", ",") + ";"}
        self.send_request_and_check(params)
        params = {"firstPoint": str(x1).replace(".", ",") , "secondPoint": str(x2).replace(".", ",") + ";" + str(y2)}
        self.send_request_and_check(params)
        params = {"secondPoint": str(x2).replace(".", ",") + ";" + str(y2).replace(".", ",")}
        self.send_request_and_check(params)
        params = {"firstPoint": str(x1).replace(".", ",") + ";" + str(y1).replace(".", ",")}
        self.send_request_and_check(params)
        params = {"firstPoint": str(x1).replace(".", ",") , "secondPoint": str(x2).replace(".", ",") + str(y2).replace(".", ",")}
        self.send_request_and_check(params)

    def send_request_and_check(self, params):
        """Functions check if server returns valid response for incorrect data"""
        try:
            server_answer = requests.get(self.address + "points-distance/", params = params)
        except ConnectionError:
            self.fail("No connection with server")
        self.assertTrue(server_answer.status_code == 400, msg = "Server should return status code 400")
        self.assertTrue(len(server_answer.text) == 0, "Answer text should be empty")


    

