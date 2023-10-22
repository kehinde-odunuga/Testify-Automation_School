import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Challenge 2

# Using the firefox browser, navigate to https://www.google.com/ and enter the text python in the search box,
# then send the enter key. Get the text from the Wikipedia brief on the right side and print the value in the console.


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://google.com/")
    driver.maximize_window()
    time.sleep(2)

    send_keys_to_element(driver.find_element(By.NAME, "q"), "Python", Keys.ENTER)
    time.sleep(5)
    wikipedia_text = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/span[1]')

    print("Python Wikipedia Text:", wikipedia_text.text)
    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    main()