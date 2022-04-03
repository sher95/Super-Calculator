import time
import traceback
import pytest
from selenium.webdriver.common.by import By
from Tests.locators import Locators
from Utilities.read_properties import read_Config

calculator = read_Config.get_url()  # If this line will give error, then just comment it and comment out line in the below
# calculator = "http://juliemr.github.io/protractor-demo/"


@pytest.mark.usefixtures("chrome_setup")
class BaseTest:
    pass


class Test_End_to_End1(BaseTest):
    def test_end_to_end_title(self):
        self.driver.get(calculator)
        self.driver.implicitly_wait(5)
        title = self.driver.find_element(By.XPATH, Locators.title_loc)
        if title.text == "Super Calculator":
            assert True
        else:
            traceback.format_exc()
            assert False


class Test_End_to_End2(BaseTest):
    def test_end_to_end_addition(self):
        self.driver.get(calculator)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, Locators.first_number_input_loc).send_keys(8)
        self.driver.find_element(By.CSS_SELECTOR, Locators.second_number_input_loc).send_keys(8)
        self.driver.find_element(By.CSS_SELECTOR, Locators.operator_loc).click()
        self.driver.find_element(By.XPATH, Locators.operator_addition_loc).click()
        self.driver.find_element(By.ID, Locators.go_button_loc).click()
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, Locators.summ_loc)
        if element.text == "16":
            assert True
        else:
            traceback.format_exc()
            assert False
        self.driver.quit()


class Test_End_to_End3(BaseTest):
    def test_end_to_end_division(self):
        self.driver.get(calculator)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, Locators.first_number_input_loc).send_keys(16)
        self.driver.find_element(By.CSS_SELECTOR, Locators.second_number_input_loc).send_keys(4)
        self.driver.find_element(By.CSS_SELECTOR, Locators.operator_loc).click()
        self.driver.find_element(By.XPATH, Locators.operator_division_loc).click()
        self.driver.find_element(By.ID, Locators.go_button_loc).click()
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, Locators.summ_loc)
        if element.text == "4":
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_end_to_end_multiplication(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.first_number_input_loc).send_keys(4)
        self.driver.find_element(By.CSS_SELECTOR, Locators.second_number_input_loc).send_keys(4)
        self.driver.find_element(By.CSS_SELECTOR, Locators.operator_loc).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.operator_multiplication_loc).click()
        self.driver.find_element(By.ID, Locators.go_button_loc).click()
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, Locators.summ_loc)
        if element.text == "16":
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_end_to_end_expression(self):
        expression = self.driver.find_elements(By.XPATH, "/html/body/div/table/tbody")
        count = int(len(expression))
        if count == 1:
            assert True
        else:
            traceback.format_exc()
            assert False
