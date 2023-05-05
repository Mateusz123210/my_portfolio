import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ArithmeticAverageSeleniumTestsCases(unittest.TestCase):

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
        page = self.driver.find_element(By.ID, "arithmeticAverage")
        page.click()
        time.sleep(self.time_sleep)
        numbers_text_field = self.driver.find_element(By.ID, "numbers")
        numbers_text_field_text = numbers_text_field.get_attribute("value")
        self.assertEqual(len(numbers_text_field_text), 0, "Numbers text field should be empty on start")
        result = self.driver.find_element(By.ID, "result")
        result_text = result.text
        self.assertEqual(len(result_text), 0, "Result should be empty on start")
        hint = self.driver.find_elements(By.ID, "hint")
        self.assertTrue(len(hint) == 0, msg = "Hint text area should not be on the page")
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
        numbers_text_field.send_keys("4;5;6;4;3;5;4;3;4;4,5")
        time.sleep(self.time_sleep)
        add_numbers_button = self.driver.find_element(By.ID, "addNumbers")
        add_numbers_button.click()
        time.sleep(self.time_sleep)        
        added_numbers = self.driver.find_element(By.ID, "writtenNumbers")
        added_numbers_text = added_numbers.get_attribute("value")
        self.assertEqual(added_numbers_text, "4;5;6;4;3;5;4;3;4;4,5", msg = "Numbers should be added")
        numbers_text_field_text = numbers_text_field.get_attribute("value")
        self.assertEqual(numbers_text_field_text, "", msg = "Numers text field should be empty")
        numbers_text_field.send_keys("4")
        time.sleep(self.time_sleep)  
        add_numbers_button.click()
        time.sleep(self.time_sleep)  
        added_numbers_text = added_numbers.get_attribute("value")
        self.assertEqual(added_numbers_text, "4;5;6;4;3;5;4;3;4;4,5;4", msg = "Number 4 should be added")
        numbers_text_field_text = numbers_text_field.get_attribute("value")
        self.assertEqual(numbers_text_field_text, "", msg = "Numbers text field should be empty")
        numbers_text_field.send_keys("4")
        solve_button = self.driver.find_element(By.ID, "solve")
        solve_button.click()
        time.sleep(self.time_sleep)
        result_text = result.text
        self.assertTrue(len(result_text) > 0, msg = "Result should appear")
        self.assertEqual(result_text, "4,2272727272727275", msg = "Result should be correct")
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
        clear_button = self.driver.find_element(By.ID, "clear")
        clear_button.click()
        time.sleep(self.time_sleep)
        added_numbers_text = added_numbers.get_attribute("value")
        self.assertEqual(added_numbers_text, "", msg = "Added numbers text field should be empty")
        solve_button.click()
        time.sleep(self.time_sleep)
        helper_text = self.driver.find_element(By.ID, "numbers-helper-text")
        helper_text_value = helper_text.text
        self.assertEqual(helper_text_value, "Dodaj liczby najpierw", msg = "Error text should appear")
