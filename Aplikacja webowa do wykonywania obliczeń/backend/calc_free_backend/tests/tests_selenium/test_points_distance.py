import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class PointsDistanceSeleniumTestsCases(unittest.TestCase):

    def setUp(self):
        "Initializing selenium driver, going to page, maximizing window and setting break time"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://calcfree.azurewebsites.net")
        self.time_sleep = 2.0
    
    def tearDown(self):
        "Quiting selenium"
        self.driver.quit()
    
    def test_page(self):
        "Test checks if all of page functions works"
        page = self.driver.find_element(By.ID, "pointsDistance")
        page.click()
        time.sleep(self.time_sleep)
        x1 = self.driver.find_element(By.ID, "x1")
        y1 = self.driver.find_element(By.ID, "y1")
        x2 = self.driver.find_element(By.ID, "x2")
        y2 = self.driver.find_element(By.ID, "y2")
        x1_value = x1.get_attribute("value")
        y1_value = y1.get_attribute("value")
        x2_value = x2.get_attribute("value")
        y2_value = y2.get_attribute("value")
        self.assertEqual(len(x1_value), 0, "X1 should be empty on start")
        self.assertEqual(len(y1_value), 0, "Y1 should be empty on start")
        self.assertEqual(len(x2_value), 0, "X2 should be empty on start")
        self.assertEqual(len(y2_value), 0, "Y2 should be empty on start")
        x1.send_keys("5,2")
        time.sleep(self.time_sleep)
        y1.send_keys("3,1")
        time.sleep(self.time_sleep)
        x2.send_keys("8,2")
        time.sleep(self.time_sleep)
        y2.send_keys("7,0")
        time.sleep(self.time_sleep)
        result = self.driver.find_element(By.ID, "result")
        result_text = result.text
        self.assertEqual(len(result_text), 0, "Result should be empty on start")
        hint = self.driver.find_elements(By.ID, "hint")
        self.assertTrue(len(hint) == 0, msg = "Hint text area should not be on the page")
        graph = self.driver.find_element(By.ID, "image")
        graph_old = graph.screenshot_as_png      
        solve_button = self.driver.find_element(By.ID, "solve")
        solve_button.click()
        time.sleep(self.time_sleep)
        result_text = result.text
        self.assertTrue(len(result_text) > 0, msg = "Result should appear")
        self.assertEqual(result_text, "d = 4,920365840057017", msg = "Result should be correct")
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