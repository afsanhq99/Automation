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


if __name__ == "__main__":
    driver = webdriver.Chrome()
    signup_page = LoginPage(driver)
    signup_page.open()
    signup_page.login(
        username="john",
        password="demo"
    )

    time.sleep(5)  

    if signup_page.is_login_successful():
        print("Login was successful!")
    else:
        print("Login failed.")

    driver.quit()
