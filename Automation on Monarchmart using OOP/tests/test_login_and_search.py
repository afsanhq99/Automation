import time
from pages.browser import Browser
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage


def login_and_search():
    browser = Browser()
    try:
        browser.open_url('https://monarchmart.com/login')

        login_page = LoginPage(browser.driver)
        login_page.login('afsan.haque99@gmail.com', 'private#fuck')

        home_page = HomePage(browser.driver)
        home_page.hover_and_check_dashboard()
        home_page.search_for_product('electrics')
        time.sleep(5)

        product_page = ProductPage(browser.driver)
        product_page.click_product_and_add_to_cart(
            'Electric Grinding Machine - Purple')


        # Wait to see the results
        time.sleep(10)

    finally:
        browser.close()


if __name__ == "__main__":
    login_and_search()
