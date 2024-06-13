import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def click_product_and_add_to_cart(self, product_title):


        product_xpath = f"//h4[@title='{product_title}']"
        product_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, product_xpath)))
        product_element.click()
        print(f"Clicked on product: {product_title}")
        try:

            add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]")))

            add_to_cart_button.click()
            print(f"Added {product_title} to cart")

            # click_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            #     (By.XPATH, "//div[@class='ShoppingCart_contents__ipZ03']")))
            click_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='CheckBox_CheckBox__bIp1T ']//*[name()='svg']//*[name()='path' "
                           "and contains(@fill-rule,'evenodd')]")))

            if click_button:
                print("located")
                click_button.click()
            else:
                print("not located")
            # click_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            #     (By.XPATH, "//div[@class='CheckBox_CheckBox__bIp1T ']//*[name()='svg']//*[name()='path' "
            #                "and contains(@fill-rule,'evenodd')]")))
            # checkout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            #     (By.XPATH, "//button[normalize-space()='Checkout']")))

            # time.sleep(3)
            # click_button.click()
            # time.sleep(3)
            # checkout_button.click()

        except:
            print("cart not added")

