from django.test import TestCase
from calc_free_backend.calculations import averages
import random
import json

class ArithmeticAveragesTestCases(TestCase):
    
    def test_one_number(self):
        """Average of one number should be this number. Hint should be returned."""
        for a in range(100):
            list = []
            number = random.uniform(-100.0, 100.0)
            list.append(number)
            response = averages.solve_arithmetic_average(list, 1)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("solution" in temp.keys(), "Solution should be in json")
            self.assertTrue(abs(number -  float(temp["solution"].replace(",", "."))) < 0.000001, msg="Average should be calculated correctly")
            self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
            self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
            self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
            self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain result")
    
    def test_many_numbers(self):
        """Average of many numbers should be calculated correctly.
        Hint should be returned."""
        for a in range(100):
            numbers = random.randint(2,50)
            list = []
            for i in range(numbers):
                number = random.uniform(-100.0, 100.0)
                list.append(number)
            response = averages.solve_arithmetic_average(list, numbers)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("solution" in temp.keys(), "Solution should be in json")
            self.assertTrue(abs(sum(list)/len(list) -  float(temp["solution"].replace(",", "."))) < 0.000001, msg="Average should be calculated \
                correctly")
            self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
            self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
            self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
            self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain result")


        