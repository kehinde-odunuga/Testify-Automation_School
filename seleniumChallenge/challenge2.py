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

#def scroll_to_element(action, element):
   # action.move_to_element(element).perform()


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://google.com/")
    driver.maximize_window()
    action = ActionChains(driver)
    time.sleep(2)
    send_keys_to_element(driver.find_element(By.NAME, "q"), "Python", Keys.ENTER)
    time.sleep(5)
    wikipedia_text = driver.find_element(By.TAG_NAME, "h3")
    #scroll_to_element(action, driver.find_element(By.TAG_NAME, "h3"))
    print("Python Wikipedia Text:", wikipedia_text.text)
    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    main()