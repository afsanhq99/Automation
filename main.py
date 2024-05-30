import time
from selenium import webdriver
from login_page import LoginPage
from test_cases import test_positive_login, test_negative_username
from test_cases import test_positive_login, test_negative_password


def main():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    try:
        test_positive_login(login_page)
        print("Positive login test passed.")
    except AssertionError:
        print("Positive login test failed.")

    try:
        test_negative_username(login_page)
        print("Negative username test passed.")
    except AssertionError:
        print("Negative username test failed.")



    try:
        test_negative_password(login_page)
        print("Negative password test passed.")
    except AssertionError:
        print("Negative password test failed.")

    driver.quit()


if __name__ == "__main__":
    main()
