# from selenium import webdriver
#
#
# class Browser:
#     def __init__(self):
#         self.driver = webdriver.Edge()
#         self.driver.maximize_window()
#
#     def open_url(self, url):
#         self.driver.get(url)
#
#     def close(self):
#         self.driver.quit()


from selenium import webdriver


class Browser:
    def __init__(self):

        self.driver= webdriver.Edge()
        self.driver.maximize_window()

    def open_url(self,url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()