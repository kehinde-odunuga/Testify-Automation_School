import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def send_keys_to_element(element, *keys):
    element.send_keys(keys)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    send_keys_to_element(driver.find_element(By.NAME, "firstname"), "Kehinde")
    send_keys_to_element(driver.find_element(By.NAME, "lastname"), "Odunuga")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "test@selenium.com")
    send_keys_to_element(driver.find_element(By.NAME, "phone"), "2341231231232")
    #time.sleep(2)
    #send_keys_to_element(driver.find_element(By.NAME, "phone"), Keys.CONTROL, "v")
    time.sleep(10)


if __name__ == '__main__':
    main()