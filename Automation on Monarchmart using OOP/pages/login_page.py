from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (
            By.XPATH, "//input[@placeholder='Write your email or phone']")
        self.password_field = (
            By.XPATH, "//input[@placeholder='Enter password']")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.email_field)).send_keys(email)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_button)).click()
