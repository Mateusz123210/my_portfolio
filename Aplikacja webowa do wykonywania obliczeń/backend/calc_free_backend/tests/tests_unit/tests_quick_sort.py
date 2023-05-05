from django.test import TestCase
from calc_free_backend.calculations import sorting
import json
import random

class QuickSortTestCases(TestCase):
    
    def test_sorting_ascending(self):
        """Test if function returns numbers sorted ascending"""
        for a in range(50):
            number_of_numbers = random.randint(1,30)
            numbers = []
            for i in range(number_of_numbers):
                numbers.append(random.uniform(-1000.0, 1000.0))        
            response = sorting.quick_sort(numbers, "yes")
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, "Json shoould be valid")
            self.assertTrue("solution" in  temp.keys(),"Solution should be in json")
            response_numbers = list(temp["solution"].split(";"))
            response_numbers = [float(x.replace(",", ".")) for x in response_numbers]
            self.assertEquals(response_numbers, sorted(numbers), "Result should be valid")
            self.check_hint(temp)

    def test_sorting_descending(self):
        """Test if function returns numbers sorted descending"""
        for a in range(50):
            number_of_numbers = random.randint(1,30)
            numbers = []
            for i in range(number_of_numbers):
                numbers.append(random.uniform(-1000.0, 1000.0))        
            response = sorting.quick_sort(numbers, "no")
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, "Json shoould be valid")
            self.assertTrue("solution" in  temp.keys(),"Solution should be in json")
            response_numbers = list(temp["solution"].split(";"))
            response_numbers = [float(x.replace(",", ".")) for x in response_numbers]
            tmp = sorted(numbers)
            tmp.reverse()
            self.assertEquals(response_numbers, tmp, "Result should be valid")
            self.check_hint(temp)
    
    def check_hint(self, temp):
        """Function checks if hint and graph are in solution"""
        self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
        self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length grater than 0)")
        self.assertTrue("Liczba wykonanych zamian" in temp["hint"], msg = "Hint should contain information \
            about number of done exchanges")