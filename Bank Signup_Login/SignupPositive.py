import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        self.success_locator = (By.XPATH, "//h1[@class='title']")
        self.welcome_locator = (By.XPATH, "//p[@class='smallText']")

    def open(self):
        self.driver.get(self.URL)

    def signup(self, firstname, lastname, address, city, state, zip_code, phone, ssn, username, password, conf_password):
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

    def is_signup_successful(self):
        success_message = self.driver.find_element(*self.success_locator)
        return success_message.is_displayed()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    signup_page = SignupPage(driver)
    signup_page.open()
    signup_page.signup(
        firstname="John",
        lastname="Doe",
        address="123 Elm Street",
        city="Anytown",
        state="CA",
        zip_code="90210",
        phone="555-1234",
        ssn="123-45-6789",
        username="johndoe",
        password="password123",
        conf_password="password123"
    )

    # Wait for the registration to process
    time.sleep(5)  
    if signup_page.is_signup_successful():
        print("Signup was successful!")
    else:
        print("Signup failed.")

    driver.quit()
