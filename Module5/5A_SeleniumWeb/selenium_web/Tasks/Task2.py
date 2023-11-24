import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Module 4A Task 2

# 1. Visit the website https://academy.testifyltd.com/
# 2. Locate the button with the text "Explore Courses" and print out the element
# 3. Locate the element with the text "Subscribe to receive training updates from Testify" and print it.

def locate_by_xpath(driver):
    explore_courses = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button/span[1]')
    print("Explore Courses:", explore_courses)



def locate_by_id(driver):
    subscribe_text = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-\[\#FCFCFC\].dark\:bg-\[\#013069\].pt-16.md\:pt-20.lg\:pt-28.pb-24.md\:pb-28.lg\:pb-32.xl\:pb-36 > div > div > div.w-full.md\:w-5\/12.xl\:w-4\/12 > h2")
    print("Subscribe Text:", subscribe_text)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    locate_by_xpath(driver)
    locate_by_id(driver)


if __name__ == '__main__':
    main()