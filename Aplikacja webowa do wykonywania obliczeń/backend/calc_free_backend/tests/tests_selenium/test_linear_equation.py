import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LinearEquationSeleniumTestsCases(unittest.TestCase):

    def setUp(self):
        "Initializing selenium driver, going to page, maximizing window and setting break time"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://calcfree.azurewebsites.net")
        self.time_sleep = 2.3
    
    def tearDown(self):
        "Quiting selenium"
        self.driver.quit()
    
    def test_page(self):
        "Test checks if all of page functions works"
        page = self.driver.find_element(By.ID, "linearEquation")
        page.click()
        time.sleep(self.time_sleep)
        equation_text_field = self.driver.find_element(By.ID, "equation")
        equation_text_field_text = equation_text_field.text
        self.assertEqual(len(equation_text_field_text), 0, "Equation should be empty on start")
        result = self.driver.find_element(By.ID, "result")
        result_text = result.text
        self.assertEqual(len(result_text), 0, "Result should be empty on start")
        hint = self.driver.find_elements(By.ID, "hint")
        self.assertTrue(len(hint) == 0, msg = "Hint text area should not be on the page")
        graph = self.driver.find_element(By.ID, "image")
        graph_old = graph.screenshot_as_png
        popover = self.driver.find_elements(By.ID, "popoverBody")
        self.assertEqual(len(popover), 0, msg = "Popover should not be open")
        popover_button = self.driver.find_element(By.ID, "popoverButton")
        popover_button.click()
        time.sleep(self.time_sleep)
        popover = self.driver.find_element(By.ID, "popoverBody")
        popover.click()
        time.sleep(self.time_sleep)
        popover = self.driver.find_elements(By.ID, "popoverBody")
        self.assertEqual(len(popover), 0, msg = "Popover should not be open")
        equation_text_field.send_keys("7x+14")
        time.sleep(self.time_sleep)
        solve_button = self.driver.find_element(By.ID, "solve")
        solve_button.click()
        time.sleep(self.time_sleep)
        result_text = result.text
        self.assertTrue(len(result_text) > 0, msg = "Result should appear")
        self.assertEqual(result_text, "x = -2,0", msg = "Result should be correct")
        hint_button = self.driver.find_element(By.ID, "hintButton")
        hint_button.click()
        time.sleep(self.time_sleep)
        hint = self.driver.find_element(By.ID, "hint")
        hint_text = hint.text
        self.assertTrue(len(hint_text) > 0, msg = "Hint text should appear")
        hint_button.click()
        time.sleep(self.time_sleep)
        hint = self.driver.find_elements(By.ID, "hint")
        self.assertTrue(len(hint) == 0, msg = "Hint text area should not be on the page")
        graph_new = graph.screenshot_as_png
        self.assertNotEqual(graph_old, graph_new, "New graph should appear")