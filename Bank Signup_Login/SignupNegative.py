import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:
    URL = "https://parabank.parasoft.com/parabank/register.htm"

    def __init__(self, driver):
        self.driver = driver
        self.firstname_locator = (
            By.XPATH, "//input[@id='customer.firstName']")
        self.lastname_locator = (By.XPATH, "//input[@id='customer.lastName']")
        self.address_locator = (
            By.XPATH, "//input[@id='customer.address.street']")
        self.city_locator = (By.XPATH, "//input[@id='customer.address.city']")
        self.state_locator = (
            By.XPATH, "//input[@id='customer.address.state']")
        self.zip_locator = (
            By.XPATH, "//input[@id='customer.address.zipCode']")
        self.phone_locator = (By.XPATH, "//input[@id='customer.phoneNumber']")
        self.ssn_locator = (By.XPATH, "//input[@id='customer.ssn']")
        self.username_locator = (By.XPATH, "//input[@id='customer.username']")
        self.pass_locator = (By.XPATH, "//input[@id='customer.password']")
        self.confpass_locator = (By.XPATH, "//input[@id='repeatedPassword']")
        self.submit_locator = (By.XPATH, "//input[@value='Register']")
        self.error_message_locator = (By.XPATH, "//span[@class='error']")

    def open(self):
        self.driver.get(self.URL)

    def clear_fields(self):
        fields = [
            self.firstname_locator, self.lastname_locator, self.address_locator,
            self.city_locator, self.state_locator, self.zip_locator, self.phone_locator,
            self.ssn_locator, self.username_locator, self.pass_locator, self.confpass_locator
        ]
        for field in fields:
            self.driver.find_element(*field).clear()

    def signup(self, firstname="", lastname="", address="", city="", state="", zip_code="", phone="", ssn="", username="", password="", conf_password=""):
        self.driver.find_element(*self.firstname_locator).send_keys(firstname)
        self.driver.find_element(*self.lastname_locator).send_keys(lastname)
        self.driver.find_element(*self.address_locator).send_keys(address)
        self.driver.find_element(*self.city_locator).send_keys(city)
        self.driver.find_element(*self.state_locator).send_keys(state)
        self.driver.find_element(*self.zip_locator).send_keys(zip_code)
        self.driver.find_element(*self.phone_locator).send_keys(phone)
        self.driver.find_element(*self.ssn_locator).send_keys(ssn)
        self.driver.find_element(*self.username_locator).send_keys(username)
        self.driver.find_element(*self.pass_locator).send_keys(password)
        self.driver.find_element(
            *self.confpass_locator).send_keys(conf_password)
        self.driver.find_element(*self.submit_locator).click()

    def get_error_messages(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.error_message_locator)
        )
        error_elements = self.driver.find_elements(*self.error_message_locator)
        return [element.text for element in error_elements]


if __name__ == "__main__":
    driver = webdriver.Chrome()
    signup_page = SignupPage(driver)
    signup_page.open()

    # Test Case 1: Leave all fields empty
    signup_page.clear_fields()
    signup_page.signup()
    error_messages = signup_page.get_error_messages()
    print("Test Case 1: Leave all fields empty")
    print("Error Messages:", error_messages)

    # Test Case 2: Only fill the first name and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(firstname="John")
    error_messages = signup_page.get_error_messages()
    print("Test Case 2: Only fill the first name and leave other fields empty")
    print("Error Messages:", error_messages)
    

    # You can continue with similar test cases for each field...
    # Test Case 3: Only fill the last name and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(lastname="Doe")
    error_messages = signup_page.get_error_messages()
    print("Test Case 3: Only fill the last name and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 4: Only fill the address and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(address="123 Main St")
    error_messages = signup_page.get_error_messages()
    print("Test Case 4: Only fill the address and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 5: Only fill the city and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(city="Anytown")
    error_messages = signup_page.get_error_messages()
    print("Test Case 5: Only fill the city and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 6: Only fill the state and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(state="CA")
    error_messages = signup_page.get_error_messages()
    print("Test Case 6: Only fill the state and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 7: Only fill the zip code and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(zip_code="12345")
    error_messages = signup_page.get_error_messages()
    print("Test Case 7: Only fill the zip code and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 8: Only fill the phone number and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(phone="1234567890")
    error_messages = signup_page.get_error_messages()
    print("Test Case 8: Only fill the phone number and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 9: Only fill the SSN and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(ssn="123456789")
    error_messages = signup_page.get_error_messages()
    print("Test Case 9: Only fill the SSN and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 10: Only fill the username and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(username="john123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 10: Only fill the username and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 11: Only fill the password and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 11: Only fill the password and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 12: Only fill the confirm password and leave other fields empty
    signup_page.clear_fields()
    signup_page.signup(conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 12: Only fill the confirm password and leave other fields empty")
    print("Error Messages:", error_messages)

    # Test Case 13: Fill all fields except the first name
    signup_page.clear_fields()
    signup_page.signup(lastname="Doe", address="123 Main St", city="Anytown", state="CA", zip_code="12345",
                    phone="1234567890", ssn="123456789", username="john123", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 13: Fill all fields except the first name")
    print("Error Messages:", error_messages)

    # Test Case 14: Fill all fields except the last name
    signup_page.clear_fields()
    signup_page.signup(firstname="John", address="123 Main St", city="Anytown", state="CA", zip_code="12345",
                    phone="1234567890", ssn="123456789", username="john123", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 14: Fill all fields except the last name")
    print("Error Messages:", error_messages)

    # Test Case 15: Fill all fields except the address
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", city="Anytown", state="CA", zip_code="12345",
                    phone="1234567890", ssn="123456789", username="john123", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 15: Fill all fields except the address")
    print("Error Messages:", error_messages)

    # Test Case 16: Fill all fields except the city
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", address="123 Main St", state="CA", zip_code="12345",
                    phone="1234567890", ssn="123456789", username="john123", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 16: Fill all fields except the city")
    print("Error Messages:", error_messages)

    # Test Case 17: Fill all fields except the state
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", address="123 Main St", city="Anytown", zip_code="12345",
                    phone="1234567890", ssn="123456789", username="john123", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 17: Fill all fields except the state")
    print("Error Messages:", error_messages)

    # Test Case 18: Fill all fields except the zip code
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", address="123 Main St", city="Anytown", state="CA",
                    phone="1234567890", ssn="123456789", username="john123", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 18: Fill all fields except the zip code")
    print("Error Messages:", error_messages)

    # Test Case 19: Fill all fields except the phone number
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", address="123 Main St", city="Anytown", state="CA",
                    zip_code="12345", ssn="123456789", username="john123", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 19: Fill all fields except the phone number")
    print("Error Messages:", error_messages)

    # Test Case 20: Fill all fields except the SSN
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", address="123 Main St", city="Anytown", state="CA",
                    zip_code="12345", phone="1234567890", username="john123", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 20: Fill all fields except the SSN")
    print("Error Messages:", error_messages)

    # Test Case 21: Fill all fields except the username
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", address="123 Main St", city="Anytown", state="CA",
                    zip_code="12345", phone="1234567890", ssn="123456789", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 21: Fill all fields except the username")
    print("Error Messages:", error_messages)

    # Test Case 22: Fill all fields except the password
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", address="123 Main St", city="Anytown", state="CA",
                    zip_code="12345", phone="1234567890", ssn="123456789", username="john123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 22: Fill all fields except the password")
    print("Error Messages:", error_messages)

    # Test Case 23: Fill all fields except the confirm password
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", address="123 Main St", city="Anytown", state="CA",
                    zip_code="12345", phone="1234567890", ssn="123456789", username="john123", password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 23: Fill all fields except the confirm password")
    print("Error Messages:", error_messages)

    # Test Case 24: Fill all fields
    signup_page.clear_fields()
    signup_page.signup(firstname="John", lastname="Doe", address="123 Main St", city="Anytown", state="CA", zip_code="12345",
                    phone="1234567890", ssn="123456789", username="john123", password="password123", conf_password="password123")
    error_messages = signup_page.get_error_messages()
    print("Test Case 24: Fill all fields")
    print("Error Messages:", error_messages)

    driver.quit()


