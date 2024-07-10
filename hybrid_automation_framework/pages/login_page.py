# pages/login_page.py
from selenium.webdriver.common.by import By
from base.base_class import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage(BaseClass):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")
    ERROR = (By.ID, "error")
    LOGOUT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[1]/a[1]")

    def enter_username(self, username):
        self.send_keys(self.USERNAME, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def click_submit(self):
        self.click(self.SUBMIT)

    def get_error_message(self):
        return self.get_text(self.ERROR)

    def is_logout_button_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGOUT))
            return True
        except TimeoutException:
            return False

    def click_logout(self):
        self.click(self.LOGOUT)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()