from django.test import TestCase
from calc_free_backend.calculations import averages
import json
import random

class WeightedAveragesTestCases(TestCase):

    def test_one_number(self):
        """Average of one number should be this number. Hint should be returned."""
        for a in range(100):
            numbers_list = []
            number = random.uniform(-100.0, 100.0)
            numbers_list.append(number)
            wages_list = []
            wage = random.uniform(0.1, 100.0)
            wages_list.append(wage)
            response = averages.solve_weighted_average(numbers_list, wages_list, 1)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("solution" in temp.keys(), "Solution should be in json")
            self.assertTrue(abs(number -  float(temp["solution"].replace(",", "."))) < 0.000001, msg="Average should be calculated correctly")
            self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
            self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
            self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
            self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")
    
    def test_many_numbers(self):
        """Average of many numbers should be calculated correctly.
        Hint should be returned."""
        for a in range(100):
            numbers = random.randint(2,50)
            numbers_list = []
            wages_list = []
            for i in range(numbers):
                number = random.uniform(-100.0, 100.0)
                numbers_list.append(number)
                wage = random.uniform(0.1, 100.0)
                wages_list.append(wage)

            response = averages.solve_weighted_average(numbers_list, wages_list, numbers)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("solution" in temp.keys(), "Solution should be in json")
            average_sum = 0.0 
            for a in range(numbers):
                average_sum += numbers_list[a] * wages_list[a] 
            self.assertTrue(abs(average_sum/sum(wages_list) -  float(temp["solution"].replace(",", "."))) < 0.000001,
             msg="Average should be calculated correctly")
            self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
            self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
            self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
            self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")

    def test_sum_of_wages_equals_zero(self):
        """When sum of wages equals 0, should return error"""
        numbers_list = []
        wages_list = []
        number = random.uniform(-100.0, 100.0)
        numbers_list.append(number)
        wage = 0.0
        wages_list.append(wage)
        response = averages.solve_weighted_average(numbers_list, wages_list, 1)
        self.assertTrue(type(response) == str, msg="Function should return string")
        temp = json.loads(response)
        self.assertTrue(type(temp) == dict, msg="Json should be valid")
        self.assertTrue("error" in temp.keys(), "Error should be in json")
        self.assertFalse("solution" in temp.keys(), "Solution should not be in json")
        self.assertFalse("hint" in temp.keys(), msg="Hint should not be in json")
    
    def test_negative_wage(self):
        """When minimum one of wages is negative function should return None"""
        numbers_list = []
        wages_list = []
        number = random.uniform(-100.0, 100.0)
        numbers_list.append(number)
        wage = random.uniform(-100.0, 100.0)
        wages_list.append(wage)
        numbers_list.append(50.0)
        wages_list.append(-2.0)
        response = averages.solve_weighted_average(numbers_list, wages_list, 1)
        self.assertTrue(response is None, msg="Function should return None")
