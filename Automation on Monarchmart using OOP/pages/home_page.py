from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.avatar_button = (By.XPATH, "//div[@class='Header_avatar__kxT1i']")
        self.dashboard_element = (
            By.XPATH, "//h2[normalize-space() = 'Dashboard']")
        self.search_bar = (
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[2]/form[1]/input[1]")

    def hover_and_check_dashboard(self):
        avatar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.avatar_button))
        ActionChains(self.driver).move_to_element(avatar).perform()
        dashboard_present = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.dashboard_element))
        if dashboard_present:
            print(
                "Login successful, 'Dashboard' element is present after hovering over the button.")
        else:
            print(
                "Login failed or 'Dashboard' element is not present after hovering over the button.")

    def search_for_product(self, product_name):
        search_bar_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_bar))
        search_bar_element.send_keys(product_name)
        search_bar_element.submit()




