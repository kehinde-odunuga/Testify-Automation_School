import time
from tasPageTask5 import tasPageTask5
from ststPageTask5 import ststPageTask5
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Module 4A Task 5

# 1. Create a page object model for this page https://academy.testifyltd.com/courses/test-automation-simplified
# 2. Create another object model for this page https://academy.testifyltd.com/courses/switch-to-software-testing
# The web elements in each of your object models should not be more than 5.


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    tas_Page = tasPageTask5(driver)
    print(tas_Page.title.text)
    stst_page = ststPageTask5(driver)
    print(stst_page.title.text)
    time.sleep(10)





if __name__ == '__main__':
    main()