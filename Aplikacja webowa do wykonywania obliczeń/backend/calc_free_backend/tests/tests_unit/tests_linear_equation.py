from django.test import TestCase
from calc_free_backend.calculations import linear_equation
import json
import random
from threading import Lock

class LinearEquationTestCases(TestCase):

    def setUp(self):
        """Initializing of Lock for matplotlib"""
        self.lck = Lock()

    def test_valid_full_equation(self):
        """Function should return valid solution, hint and function graph."""
        for a in range(5):
            x = random.uniform(-100.0, -0.1)
            rest = random.uniform(-100.0, -0.1)
            equation = str(x) + "x" + str(rest)
            response = linear_equation.solve_linear_equation(equation, self.lck)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("solution" in temp.keys(), "Solution should be in json")
            self.assertTrue(abs((-rest/x) -  float(temp["solution"][4:].replace(",", "."))) < 0.000001, 
                msg="Solution should be calculated correctly")
            self.check_hint_and_graph(temp)
    
    def test_valid_equation_without_b(self):
        """Function should return valid solution, hint and function graph. 
        Parameter b is not written in equation"""
        x = random.uniform(-100.0, -0.1)
        equation = str(x) + "x"
        response = linear_equation.solve_linear_equation(equation, self.lck)
        self.assertTrue(type(response) == str, msg="Function should return string")
        temp = json.loads(response)
        self.assertTrue(type(temp) == dict, msg="Json should be valid")
        self.assertTrue("solution" in temp.keys(), "Solution should be in json")
        self.assertTrue(abs((-0/x) -  float(temp["solution"][4:].replace(",", "."))) < 0.000001, msg="Solution should be calculated correctly")
        self.check_hint_and_graph(temp)
    
    def test_valid_equation_without_a(self):
        """Function should return valid solution, hint and function graph. 
        Parameter a is not written in equation"""
        rest = random.uniform(-100.0, -0.1)
        equation = "x" + str(rest)
        response = linear_equation.solve_linear_equation(equation, self.lck)
        self.assertTrue(type(response) == str, msg="Function should return string")
        temp = json.loads(response)
        self.assertTrue(type(temp) == dict, msg="Json should be valid")
        self.assertTrue("solution" in temp.keys(), "Solution should be in json")
        self.assertTrue(abs((-rest/1) -  float(temp["solution"][4:].replace(",", "."))) < 0.000001, 
            msg="Solution should be calculated correctly")
        self.check_hint_and_graph(temp)

    def test_valid_equation_without_a_and_b(self):
        """Function should return valid solution, hint and function graph. 
        Parameters a and b are not written in equation"""
        equation = "x"
        response = linear_equation.solve_linear_equation(equation, self.lck)
        self.assertTrue(type(response) == str, msg="Function should return string")
        temp = json.loads(response)
        self.assertTrue(type(temp) == dict, msg="Json should be valid")
        self.assertTrue("solution" in temp.keys(), "Solution should be in json")
        self.assertTrue(abs(0.0 -  float(temp["solution"][4:].replace(",", "."))) < 0.000001, 
            msg="Solution should be calculated correctly")
        self.check_hint_and_graph(temp)

    def test_zero_parameter(self):
        """Quadratic equation does not exist, when parametr a is 0.
        Function should return None, because function with parameter a equals 0
        is not quadratic"""
        equation = "0x^2+5x+6"
        response = linear_equation.solve_linear_equation(equation, self.lck)
        self.assertTrue(response is None, msg="Function should return None")

    def check_hint_and_graph(self, temp):
        """Functions checks if hint and graph are in solution"""
        self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
        self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
        self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
        self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")
        self.assertTrue("graph" in temp.keys(), msg="Graph should be in json")