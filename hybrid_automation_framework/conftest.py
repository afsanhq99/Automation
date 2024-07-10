# conftest.py
import pytest
from selenium import webdriver
from utilities.config_reader import read_config
import os
from datetime import datetime


@pytest.fixture(scope="function")
def setup(request):
    config = read_config()
    browser = config['DEFAULT']['browser']
    url = config['DEFAULT']['url']

    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get(url)
    driver.maximize_window()

    yield driver

    # Capture screenshot on test failure
    if request.node.rep_call.failed:
        take_screenshot(driver, request.node.name)

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


def take_screenshot(driver, name):
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_file = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved to {screenshot_file}")


