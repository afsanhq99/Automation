import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC"

    def __init__(self, driver):
        self.driver = driver
        self.user_locator = (By.XPATH, "//input[@name='username']")
        self.pass_locator = (By.XPATH, "//input[@name='password']")
        self.login_locator = (By.XPATH, "//input[@value='Log In']")
        self.loginsuccess_locator = (
            By.XPATH, "//a[normalize-space()='Log Out']")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.user_locator).send_keys(username)
        self.driver.find_element(*self.pass_locator).send_keys(password)
        self.driver.find_element(*self.login_locator).click()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located(self.loginsuccess_locator)
            )
            return self.driver.find_element(*self.loginsuccess_locator).is_displayed()
        except:
            return False


def run_all_tests():
    driver = webdriver.Chrome()

    # Test invalid username
    signup_page = LoginPage(driver)
    signup_page.open()
    signup_page.login(
        username="invalid_user",
        password="demo"
    )
    time.sleep(2)
    if signup_page.is_login_successful():
        print("Test failed: Invalid username should not log in successfully.")
    else:
        print("Test passed: Invalid username did not log in.")

    # Test invalid password
    signup_page.open()
    signup_page.login(
        username="john",
        password="invalid_pass"
    )
    time.sleep(2)
    if signup_page.is_login_successful():
        print("Test failed: Invalid password should not log in successfully.")
    else:
        print("Test passed: Invalid password did not log in.")

    # Test empty username
    signup_page.open()
    signup_page.login(
        username="",
        password="demo"
    )
    time.sleep(2)
    if signup_page.is_login_successful():
        print("Test failed: Empty username should not log in successfully.")
    else:
        print("Test passed: Empty username did not log in.")

    # Test empty password
    signup_page.open()
    signup_page.login(
        username="john",
        password=""
    )
    time.sleep(2)
    if signup_page.is_login_successful():
        print("Test failed: Empty password should not log in successfully.")
    else:
        print("Test passed: Empty password did not log in.")

    # Test SQL injection username
    signup_page.open()
    signup_page.login(
        username="'; DROP TABLE users; --",
        password="demo"
    )
    time.sleep(2)
    if signup_page.is_login_successful():
        print("Test failed: SQL injection username should not log in successfully.")
    else:
        print("Test passed: SQL injection username did not log in.")

    # Test SQL injection password
    signup_page.open()
    signup_page.login(
        username="john",
        password="' OR '1'='1"
    )
    time.sleep(2)
    if signup_page.is_login_successful():
        print("Test failed: SQL injection password should not log in successfully.")
    else:
        print("Test passed: SQL injection password did not log in.")

    driver.quit()


if __name__ == "__main__":
    run_all_tests()
