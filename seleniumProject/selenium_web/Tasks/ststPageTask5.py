
from selenium.webdriver.common.by import By


class ststPageTask5:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/switch-to-software-testing")
        self.title = driver.find_element(By.TAG_NAME, "h1")