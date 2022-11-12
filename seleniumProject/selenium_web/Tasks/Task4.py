import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Module 4A Task 4

# Navigate to the website https://www.facebook.com/
# 1. Find the email box and enter an email value
# 2. Find the password box and enter a password value
# 3. Find the Login button and click it


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://facebook.com/")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "test@selenium.com")
    send_keys_to_element(driver.find_element(By.NAME, "pass"), "12345678")
    time.sleep(3)
    driver.find_element(By.NAME, "login" ).click()
    time.sleep(10)


if __name__ == '__main__':
    main()