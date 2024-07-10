# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from utilities.excel_utils import get_test_data
from utilities.logger import setup_logger
import os

logger = setup_logger(os.path.join('reports', 'test_login.log'))

# Get test data from Excel file
test_data = get_test_data(os.path.join('test_data', 'test_data.xlsx'), 'Sheet1')


@pytest.mark.parametrize("username, password", test_data)
def test_login(setup, username, password):
    driver = setup
    login_page = LoginPage(driver)

    logger.info(f"Testing login with username: {username} and password: {password}")

    login_page.login(username, password)

    if login_page.is_logout_button_visible():
        logger.info("Login successful")
        login_page.click_logout()
        assert True, "Login successful"
    else:
        error_message = login_page.get_error_message()
        logger.info(f"Login failed. Error message: {error_message}")
        assert False, f"Login failed. Error message: {error_message}"