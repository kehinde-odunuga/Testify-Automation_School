import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Challenge 1

# Using the chrome browser, navigate to https://www.facebook.com/ fill the email/phone box and password text box then click the Login button.


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://facebook.com/")
    driver.maximize_window()
    time.sleep(2)
    send_keys_to_element(driver.find_element(By.NAME, "email"), "test@selenium.com")
    time.sleep(2)
    send_keys_to_element(driver.find_element(By.NAME, "pass"), "12345678")
    time.sleep(2)
    driver.find_element(By.NAME, "login" ).click()
    time.sleep(5)


if __name__ == '__main__':
    main()