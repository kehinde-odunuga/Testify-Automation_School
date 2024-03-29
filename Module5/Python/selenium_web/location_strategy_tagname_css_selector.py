import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_tag_name(driver):
    first_input = driver.find_element(By.TAG_NAME, "input")
    print("First Input Element:", first_input)
    div_elements = driver.find_elements(By.TAG_NAME, "div")
    print("Total Divs:", len(div_elements))
    for div_element in div_elements:
        print("Div Element:", div_element)


def locate_by_css_selector(driver):
    firstname_element = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-primary.contact-section > div > div.mt-12.lg\:mt-16.w-full.xl\:w-11\/12.mx-auto.flex.flex-row.flex-wrap.items-start > div.w-full.md\:w-8\/12.bg-white.px-5.md\:px-8.xl\:px-12.pt-12.pb-14 > form > div:nth-child(1) > div:nth-child(1) > input")
    print("Firstname Element by CSS Selector", firstname_element)
    input_elements = driver.find_elements(By.CSS_SELECTOR, "div.relative")
    print("Total div.relative:", len(input_elements))
    for input_element in input_elements:
        print("div.relative Element:", input_element)


def locate_by_class_name(driver):
    rr_first_element = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("React Reveal First Element", rr_first_element)
    rr_elements = driver.find_elements(By.CLASS_NAME, "react-reveal")
    for rr_element in rr_elements:
        print("React Reveal Element", rr_elements)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    #locate_by_tag_name(driver)
    locate_by_css_selector(driver)
    #locate_by_class_name(driver)


if __name__ == '__main__':
    main()