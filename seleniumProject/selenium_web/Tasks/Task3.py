import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Module 4A Task 3

# 1. Navigate to the website https://academy.testifyltd.com/
# 2. Get the element with the text "© 2022 Testify Limited. All rights reserved."
# 3. Print out the element text, and properties, and it attributes

def print_element_text(element):
    print("Text:", element.text)


def print_element_properties(element):
    print("Properties:", element.get_property("© 2022 Testify Limited. All rights reserved."))


def print_element_attribute(element):
    print("ID:", element.get_attribute("id"))
    print("Class:", element.get_attribute("class"))
    print("Style:", element.get_attribute("style"))
    print("Inner Text:", element.get_attribute("innerText"))
    print("Inner HTML:", element.get_attribute("innerHTML"))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    element = driver.find_element(By.LINK_TEXT, "© 2022 Testify Limited. All rights reserved.")
    print_element_text(element)
    print_element_properties(element)
    print_element_attribute(element)


if __name__ == '__main__':
    main()