import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class RoutingSeleniumTestsCases(unittest.TestCase):

    def setUp(self):
        "Initializing selenium driver, going to page, maximizing window and setting break time"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://calcfree.azurewebsites.net")
        self.time_sleep = 1.8
        
    def test_routing(self):
        "Test checks, if routing between pages works correctly"
        time.sleep(self.time_sleep)
        self.go_to_the_page("Logo should be found", "Should stay on the main page",
            "logo", "https://calcfree.azurewebsites.net/")
        self.go_to_the_page("Linear equation button should be found", "Should go to page linear equation",
            "linearEquation", "https://calcfree.azurewebsites.net/linear-equation")
        self.go_to_the_page("Logo should be found", "Should go to the the main page",
            "logo", "https://calcfree.azurewebsites.net/")
        self.go_to_the_page("Square equation button should be found", "Should go to page square equation",
            "squareEquation", "https://calcfree.azurewebsites.net/square-equation")
        self.go_to_the_page("Page name should be found", "Should go to the main page",
            "pageName", "https://calcfree.azurewebsites.net/")
        self.go_to_the_page("Calculator button should be found", "Should go to calculator page",
            "calculator", "https://calcfree.azurewebsites.net/calculator")
        self.go_to_the_page("Logo should be found", "Should go to the the main page",
            "logo", "https://calcfree.azurewebsites.net/")
        self.go_to_the_page("Arithmetic average button should be found", "Should go to arithmetic average page",
            "arithmeticAverage", "https://calcfree.azurewebsites.net/arithmetic-average")
        self.go_to_the_page("Logo should be found", "Should go to the the main page",
            "logo", "https://calcfree.azurewebsites.net/")
        self.go_to_the_page("Weighted average button should be found", "Should go to weighted average page",
            "weightedAverage", "https://calcfree.azurewebsites.net/weighted-average")
        self.go_to_the_page("Logo should be found", "Should go to the the main page",
            "logo", "https://calcfree.azurewebsites.net/")
        self.go_to_the_page("BubbleSort button should be found", "Should go to bubble sort page",
            "bubbleSort", "https://calcfree.azurewebsites.net/bubble-sort")
        self.go_to_the_page("Logo should be found", "Should go to the the main page",
            "logo", "https://calcfree.azurewebsites.net/")
        self.go_to_the_page("Quck sort button should be found", "Should go to page quick sort",
            "quickSort", "https://calcfree.azurewebsites.net/quick-sort")
        self.go_to_the_page("Page name should be found", "Should go to the main page",
            "pageName", "https://calcfree.azurewebsites.net/")
        self.go_to_the_page("Points distance button should be found", "Should go to page points distance",
            "pointsDistance", "https://calcfree.azurewebsites.net/points-distance")
        self.go_to_the_page("Page name should be found", "Should go to the main page",
            "pageName", "https://calcfree.azurewebsites.net/")
        self.go_to_the_page("Triangle button should be found", "Should go to page triangle",
            "triangleCalculations", "https://calcfree.azurewebsites.net/triangle-calculations")
        self.go_to_the_page("Page name should be found", "Should go to the main page",
            "pageName", "https://calcfree.azurewebsites.net/")
          
    def go_to_the_page(self, name, name2, id, valid_link):
        "Function checks if we can go to specified page from current"
        page = self.driver.find_element(By.ID, id)
        self.assertTrue(page is not None, msg = name)
        page.click()
        time.sleep(self.time_sleep)
        current_link = self.driver.current_url
        self.assertEqual(current_link, valid_link,
            msg = name2)

    def tearDown(self):
        "Quiting selenium"
        self.driver.quit()
