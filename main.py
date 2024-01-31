from selenium import webdriver

class ChromeDriver:
    def __init__(self) -> None:
        self.browser = webdriver.Chrome()