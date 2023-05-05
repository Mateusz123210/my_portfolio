from django.test import TestCase
from calc_free_backend.calculations import square_equation
import json
import random
from threading import Lock

class SquareEquationTestCases(TestCase):

    def setUp(self):
        """Initializing of Lock for matplotlib"""
        self.lck = Lock()

    def test_valid_full_equation(self):
        """Function should return valid solution, hint and function graph."""
        for a in range(5):
            x2 = random.uniform(-100.0, 100.0)
            if x2 == 0.0: 
                x2 = 0.1
            x = random.uniform(-100.0, -0.1)
            rest = random.uniform(-100.0, -0.1)
            equation = str(x2) + "x^2" + str(x) + "x" + str(rest)
            response = square_equation.solve_square_equation(equation, self.lck)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("solution" in temp.keys(), "Solution should be in json")
            delta = x**2-4*x2*rest
            self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
            self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
            self.assertTrue("delta" in temp["hint"], msg = "Hint should contain delta")
            self.assertTrue("graph" in temp.keys(), msg="Graph should be in json")
            if delta < 0:
                self.assertTrue(temp["solution"] == "Brak rozwiązań", 
                    msg="Solution should be calculated correctly")
            elif delta == 0.0:
                sol = -x/(2*x2  ) 
                self.assertTrue(abs(sol -  float(temp["solution"][5:].replace(",", "."))) < 0.000001, 
                    msg="Solution should be calculated correctly")
                self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
                self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")
            else:
                self.assertTrue("x1" in temp["solution"], msg="x1 should be in solution")
                self.assertTrue("x2" in temp["solution"], msg="x2 should be in solution")
                self.assertTrue("Wzory" in temp["hint"], msg = "Hint should contain formula")
                self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")

    def test_valid_equation_without_b(self):
        """Function should return valid solution, hint and function graph. 
        Parameter b is not written in equation"""
        x2 = random.uniform(-100.0, 100.0)
        if x2 == 0.0: 
            x2 = 0.1
        rest = random.uniform(-100.0, -0.1)
        equation = str(x2) + "x^2" "+x" + str(rest)
        response = square_equation.solve_square_equation(equation, self.lck)
        self.assertTrue(type(response) == str, msg="Function should return string")
        temp = json.loads(response)
        self.assertTrue(type(temp) == dict, msg="Json should be valid")
        self.assertTrue("solution" in temp.keys(), "Solution should be in json")
        delta = 1**2-4*x2*rest
        self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
        self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
        self.assertTrue("delta" in temp["hint"], msg = "Hint should contain delta")
        self.assertTrue("graph" in temp.keys(), msg="Graph should be in json")
        if delta < 0:
            self.assertTrue(temp["solution"] == "Brak rozwiązań", 
                msg="Solution should be calculated correctly")
        elif delta == 0.0:
            sol = -1 / (2 * x2) 
            self.assertTrue(abs(sol -  float(temp["solution"][5:].replace(",", "."))) < 0.000001, 
                msg="Solution should be calculated correctly")
            self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
            self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")
        else:
            self.assertTrue("x1" in temp["solution"], msg="x1 should be in solution")
            self.assertTrue("x2" in temp["solution"], msg="x2 should be in solution")
            self.assertTrue("Wzory" in temp["hint"], msg = "Hint should contain formula")
            self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")

    def test_valid_equation_without_a(self):
        """Function should return valid solution, hint and function graph. 
        Parameter a is not written in equation"""
        for a in range(5):
            x = random.uniform(-100.0, -0.1)
            rest = random.uniform(-100.0, -0.1)
            equation = "x^2" + str(x) + "x" + str(rest)
            response = square_equation.solve_square_equation(equation, self.lck)
            self.assertTrue(type(response) == str, msg="Function should return string")
            temp = json.loads(response)
            self.assertTrue(type(temp) == dict, msg="Json should be valid")
            self.assertTrue("solution" in temp.keys(), "Solution should be in json")
            delta = x**2-4*1*rest
            self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
            self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
            self.assertTrue("delta" in temp["hint"], msg = "Hint should contain delta")
            self.assertTrue("graph" in temp.keys(), msg="Graph should be in json")
            if delta < 0:
                self.assertTrue(temp["solution"] == "Brak rozwiązań", 
                    msg="Solution should be calculated correctly")
            elif delta == 0.0:
                sol = -x/2.0
                self.assertTrue(abs(sol -  float(temp["solution"][5:].replace(",", "."))) < 0.000001, 
                    msg="Solution should be calculated correctly")
                self.assertTrue("Wzór" in temp["hint"], msg = "Hint should contain formula")
                self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")
            else:
                self.assertTrue("x1" in temp["solution"], msg="x1 should be in solution")
                self.assertTrue("x2" in temp["solution"], msg="x2 should be in solution")
                self.assertTrue("Wzory" in temp["hint"], msg = "Hint should contain formula")
                self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")

    def test_valid_equation_without_c(self):
        """Function should return valid solution, hint and function graph. 
        Parameter c is not written in equation"""
        x2 = random.uniform(-100.0, 100.0)
        if x2 == 0.0: 
            x2 = 0.1
        x = random.uniform(-100.0, -0.1)
        equation = str(x2) + "x^2" + str(x) + "x"
        response = square_equation.solve_square_equation(equation, self.lck)
        self.assertTrue(type(response) == str, msg="Function should return string")
        temp = json.loads(response)
        self.assertTrue(type(temp) == dict, msg="Json should be valid")
        self.assertTrue("solution" in temp.keys(), "Solution should be in json")
        delta = x**2-4*x2*0
        self.assertTrue("hint" in temp.keys(), msg="Hint should be in json")
        self.assertTrue(len(temp["hint"]) > 0, msg = "Hint should be valid(length greater than 0)")
        self.assertTrue("delta" in temp["hint"], msg = "Hint should contain delta")
        self.assertTrue("graph" in temp.keys(), msg="Graph should be in json")
        self.assertTrue("x1" in temp["solution"], msg="x1 should be in solution")
        self.assertTrue("x2" in temp["solution"], msg="x2 should be in solution")
        self.assertTrue("Wzory" in temp["hint"], msg = "Hint should contain formula")
        self.assertTrue("Wynik" in temp["hint"], msg = "Hint should contain solution")

    def test_zero_parameter(self):
        """Quadratic equation does not exist, when parametr a is 0.
        Function should return None, because function with parameter a equals 0
        is not quadratic"""
        equation = "0x^2+9x+7"
        response = square_equation.solve_square_equation(equation, self.lck)
        self.assertTrue(response is None, msg = "Function should return None")
