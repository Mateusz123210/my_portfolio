from django.test import TestCase
from calc_free_backend.calculations import triangle
import json
import random

class TriangleTestCases(TestCase):

    def test_three_sides_given(self):
        """Test checks if function returns valid solution, when all three parameters
        are given."""
        for i in range(30):
            a = random.uniform(0.000001, 10000.00)
            b = random.uniform(0.000001, 10000.00)
            c = (a**2 + b**2)**(1/2.0)
            response = triangle.calculate_triangle_properties(a, b, c)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.check_hint_and_solution(a, b, c, temp)
    
    def test_a_is_not_given(self):
        """Test checks if function returns valid solution, when parameter a is not given."""
        for i in range(30):
            b = random.uniform(0.000001, 10000.00)
            c = random.uniform(b + 0.000001, 10001.00)
            a = (c**2 - b**2)**(1 / 2.0)
            response = triangle.calculate_triangle_properties(None, b, c)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("firstSide" in temp.keys(), "Side a should be in json")
            self.assertTrue(abs(a -  float(temp["firstSide"].replace(",", "."))) < 0.000001, msg="Side a should be calculated correctly")
            self.assertTrue("Bok a" in temp["hint"], msg = "Hint should contain side a")
            self.check_hint_and_solution(a, b, c, temp)

    def test_a_is_not_given(self):
        """Test checks if function returns valid solution, when parameter a is not given."""
        for i in range(30):
            b = random.uniform(0.000001, 10000.00)
            c = random.uniform(b + 0.000001, 10001.00)
            a = (c**2 - b**2)**(1 / 2.0)
            response = triangle.calculate_triangle_properties(None, b, c)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("firstSide" in temp.keys(), "Side a should be in json")
            self.assertTrue(abs(a -  float(temp["firstSide"].replace(",", "."))) < 0.000001, 
                msg="Length of side a should be calculated correctly")
            self.assertTrue("Bok a" in temp["hint"], msg = "Hint should contain side a")
            self.check_hint_and_solution(a, b, c, temp)
    
    def test_b_is_not_given(self):
        """Test checks if function returns valid solution, when parameter b is not given."""
        for i in range(30):
            a = random.uniform(0.000001, 10000.00)
            c = random.uniform(a + 0.000001, 10001.00)
            b = (c**2 - a**2)**(1 / 2.0)
            response = triangle.calculate_triangle_properties(a, None, c)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("secondSide" in temp.keys(), "Side a should be in json")
            self.assertTrue(abs(b -  float(temp["secondSide"].replace(",", "."))) < 0.000001, 
                msg="Length of side b should be calculated correctly")
            self.assertTrue("Bok b" in temp["hint"], msg = "Hint should contain side b")
            self.check_hint_and_solution(a, b, c, temp)

    def test_c_is_not_given(self):
        """Test checks if function returns valid solution, when parameter c is not given."""
        for i in range(30):
            a = random.uniform(0.000001, 10000.00)
            b = random.uniform(0.000001, 10000.00)
            c = (a**2 + b**2)**(1 / 2.0)
            response = triangle.calculate_triangle_properties(a, b, None)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("hypotenuse" in temp.keys(), "Side c should be in json")
            self.assertTrue(abs(c -  float(temp["hypotenuse"].replace(",", "."))) < 0.000001, 
                msg="Length of side c should be calculated correctly")
            self.assertTrue("Bok c" in temp["hint"], msg = "Hint should contain side c")
            self.check_hint_and_solution(a, b, c, temp)

    def test_invalid_a_argument(self):
        "Test checks if function returns error, when a is not positive"
        for i in range(30):
            a = random.uniform(-100.0, 0.0)
            b = random.uniform(0.000001, 10000.00)
            c = (a**2 + b**2)**(1 / 2.0)
            response = triangle.calculate_triangle_properties(a, b, c)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.check_only_error_in_json(temp)

    def test_invalid_b_argument(self):
        "Test checks if function returns error, when b is not positive"
        for i in range(30):
            a = random.uniform(0.000001, 10000.00)
            b = random.uniform(-100.0, 0.0)            
            c = (a**2 + b**2)**(1 / 2.0)
            response = triangle.calculate_triangle_properties(a, b, c)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.check_only_error_in_json(temp)
    
    def test_invalid_c_argument(self):
        "Test checks if function returns error, when c is invalid"
        for i in range(30):
            a = random.uniform(0.000001, 10000.00)
            b = random.uniform(-100.0, 0.0)            
            c = (a**2 + b**2)**(1 / 2.0) - random.uniform(0.01,1000000.0)
            response = triangle.calculate_triangle_properties(a, b, c)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.check_only_error_in_json(temp)
    
    def check_only_error_in_json(self, temp):
        "Function checks whether only errror is in json"
        self.assertTrue("error" in temp.keys(), "Error should be in json")
        self.assertFalse("sinL" in temp.keys(), "Sine alfa should not be in json")
        self.assertFalse("cosL" in temp.keys(), "Cosine alfa should not be in json")
        self.assertFalse("tgL" in temp.keys(), "Tangent alfa should not be in json")
        self.assertFalse("ctgL" in temp.keys(), "Cotangent alfa should not be in json")
        self.assertFalse("hint" in temp.keys(), msg="Hint should not be in json")

    def check_hint_and_solution(self, a, b, c, temp):
        "Function checks whether trigonometric functions are in solution and hint"
        sinL = b / c
        cosL = a / c
        tgL = b / a
        ctgL = a / b
        self.assertTrue("sinL" in temp.keys(), "Sine alfa should be in json")
        self.assertTrue(abs(sinL -  float(temp["sinL"].replace(",", "."))) < 0.000001, msg="Sine alfa should be calculated correctly")
        self.assertTrue("cosL" in temp.keys(), "Cosine alfa should be in json")
        self.assertTrue(abs(cosL -  float(temp["cosL"].replace(",", "."))) < 0.000001, msg="Cosine alfa should be calculated correctly")
        self.assertTrue("tgL" in temp.keys(), "Tangent alfa should be in json")
        self.assertTrue(abs(tgL -  float(temp["tgL"].replace(",", "."))) < 0.000001, msg="Tangent alfa should be calculated correctly")
        self.assertTrue("ctgL" in temp.keys(), "Cotangent alfa should be in json")
        self.assertTrue(abs(ctgL -  float(temp["ctgL"].replace(",", "."))) < 0.000001, msg="Cotangent alfa should be calculated correctly")
        self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")  
        self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
        self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain pattern")
        self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain result")
        self.assertTrue("sin(L)" in temp["hint"], msg = "Hint should contain sine alfa")
        self.assertTrue("cos(L)" in temp["hint"], msg = "Hint should contain cosine alfa")
        self.assertTrue("tg(L)" in temp["hint"], msg = "Hint should contain tangent alfa")
        self.assertTrue("ctg(L)" in temp["hint"], msg = "Hint should contain cotangent alfa")
        self.assertTrue("sin(B)" in temp["hint"], msg = "Hint should contain sine beta")
        self.assertTrue("cos(B)" in temp["hint"], msg = "Hint should contain cosine beta")
        self.assertTrue("tg(B)" in temp["hint"], msg = "Hint should contain tangent beta")
        self.assertTrue("ctg(B)" in temp["hint"], msg = "Hint should contain cotangent beta")