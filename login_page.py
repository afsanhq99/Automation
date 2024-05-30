from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "username")
        self.password_locator = (By.ID, "password")
        self.submit_locator = (By.ID, "submit")
        self.error_locator = (By.ID, "error")
        self.logout_locator = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[1]/a[1]")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        username_input = self.driver.find_element(*self.username_locator)
        password_input = self.driver.find_element(*self.password_locator)
        submit_button = self.driver.find_element(*self.submit_locator)

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()

    def is_logged_in(self):
        return "practicetestautomation.com/logged-in-successfully/" in self.driver.current_url

    def is_logout_button_displayed(self):
        try:
            return self.driver.find_element(*self.logout_locator).is_displayed()
        except:
            return False

    def is_error_message_displayed(self):
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.error_locator)
            )
            return error_message.is_displayed()
        except:
            return False

    def get_error_message_text(self):
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.error_locator)
            )
            return error_message.text
        except:
            return ""
