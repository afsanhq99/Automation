# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
#
# class Checkout:
#     def __init__(self, driver):
#         # self.driver = driver
#         # self.cart = (By.XPATH, "//button[@title='Cart']")
#         # self.cart_button = (By.XPATH, "//div[@class='CheckBox_CheckBox__bIp1T ']//*[name()='svg']//*[name()='path' "
#         #                               "and contains(@fill-rule,'evenodd')]")
#         # # self.increase = (By.XPATH,"//div[@class='ShoppingCart_items__cyTDa']//div[2]//div[2]//div[2]//div[1]//div[1]//div[1]//button[2]//*[name()='svg']")
#         # self.checkout_button = (By.XPATH, "//button[normalize-space()='Checkout']")
#
#     def select_increase(self):
#         try:
#             cart = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable(self.cart))
#
#             button = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable(self.cart_button))
#             # increase = WebDriverWait(self.driver, 10).until(
#             #     EC.element_to_be_clickable(self.increase))
#             check = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable(self.increase))  # Assuming this is intentional
#
#             cart.click()
#             button.click()
#             increase.click()
#             check.click()
#
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")
#
#         finally:
#             # Optional: Add cleanup code here if needed
#             pass
