from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        link = "http://selenium1py.pythonanywhere.com/"
        self.browser.get(link)
	      