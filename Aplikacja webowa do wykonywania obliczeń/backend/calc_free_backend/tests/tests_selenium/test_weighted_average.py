import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WeightedAverageSeleniumTestsCases(unittest.TestCase):

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
        page = self.driver.find_element(By.ID, "weightedAverage")
        page.click()
        time.sleep(self.time_sleep)
        number_text_field = self.driver.find_element(By.ID, "number")
        number_text_field_value = number_text_field.get_attribute("value")
        self.assertEqual(len(number_text_field_value), 0, "Number text field should be empty on start")
        wage_text_field = self.driver.find_element(By.ID, "wage")
        wage_text_field_value = wage_text_field.get_attribute("value")
        self.assertEqual(len(wage_text_field_value), 0, "Wage text field should be empty on start")        
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
        number_text_field.send_keys("4,5")
        time.sleep(self.time_sleep)
        wage_text_field.send_keys("4")
        time.sleep(self.time_sleep)
        add_numbers_button = self.driver.find_element(By.ID, "addNumber")
        add_numbers_button.click()
        time.sleep(self.time_sleep)        
        added_numbers = self.driver.find_element(By.ID, "writtenNumbers")
        added_numbers_value = added_numbers.get_attribute("value")
        self.assertEqual(added_numbers_value, "4,5(4)", msg = "Number and wage should be added")
        number_text_field_value = number_text_field.get_attribute("value")
        self.assertEqual(number_text_field_value, "", msg = "Number text field should be empty")
        wage_text_field_value = wage_text_field.get_attribute("value")
        self.assertEqual(wage_text_field_value, "", msg = "wage text field should be empty")
        number_text_field.send_keys("3")
        time.sleep(self.time_sleep)
        wage_text_field.send_keys("2")
        time.sleep(self.time_sleep)
        add_numbers_button = self.driver.find_element(By.ID, "addNumber")
        add_numbers_button.click()
        time.sleep(self.time_sleep)        
        added_numbers = self.driver.find_element(By.ID, "writtenNumbers")
        added_numbers_value = added_numbers.get_attribute("value")
        self.assertEqual(added_numbers_value, "4,5(4);3(2)", msg = "Number and wage should be added")
        number_text_field_value = number_text_field.get_attribute("value")
        self.assertEqual(number_text_field_value, "", msg = "Number text field should be empty")
        wage_text_field_value = wage_text_field.get_attribute("value")
        self.assertEqual(wage_text_field_value, "", msg = "wage text field should be empty")
        solve_button = self.driver.find_element(By.ID, "solve")
        solve_button.click()
        time.sleep(self.time_sleep)
        result_text = result.text
        self.assertTrue(len(result_text) > 0, msg = "Result should appear")
        self.assertEqual(result_text, "4,0", msg = "Result should be correct")
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
        added_numbers_value= added_numbers.get_attribute("value")
        self.assertEqual(added_numbers_value, "", msg = "Added numbers text field should be empty")

        

