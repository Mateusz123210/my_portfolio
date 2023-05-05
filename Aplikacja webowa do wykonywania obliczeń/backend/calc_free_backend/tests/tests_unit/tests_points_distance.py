from django.test import TestCase
from calc_free_backend.calculations import points_on_surface
import json
import random
from threading import Lock

class pointsDistanceTestCases(TestCase):

    def setUp(self):
        """Initializing of Lock for matplotlib"""
        self.lck = Lock()
    
    def test_correct_result(self):
        """Test should check if functions return correct distance between
        points"""
        for i in range(200):
            first_point = []
            second_point = []
            first_point.append(random.uniform(-1000.0, 1000.0))
            first_point.append(random.uniform(-1000.0, 1000.0))
            second_point.append(random.uniform(-1000.0, 1000.0))
            second_point.append(random.uniform(-1000.0, 1000.0))
            response =points_on_surface.find_distance_between_points(first_point, second_point, self.lck)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("solution" in temp.keys(), "Solution should be in json")
            sol = ((first_point[0] - second_point[0])**2 + (first_point[1] - second_point[1])**2)**(1/2.0)
            self.assertTrue(abs(sol -  float(temp["solution"][4:].replace(",", "."))) < 0.000001, 
                msg="Distance should be calculated correctly")
            self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
            self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
            self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
            self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain result")

    def test_zero_distance(self):
        """Test should check if returned distance between two points, which are in the
        same position is 0"""
        for i in range(100):
            first_point = []
            first_point.append(random.uniform(-1000.0, 1000.0))
            first_point.append(random.uniform(-1000.0, 1000.0))
            response =points_on_surface.find_distance_between_points(first_point, first_point, self.lck)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("solution" in temp.keys(), "Solution should be in json")
            self.assertTrue(abs(0.0 -  float(temp["solution"][4:].replace(",", "."))) < 0.000001, 
                msg="Distance should be calculated correctly")
            self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
            self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
            self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
            self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain result")