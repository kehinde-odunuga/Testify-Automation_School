import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Challenge 4

# Navigate to https://www.bbc.com/  and  print  out  the top 10 latest news from the home page.


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    driver.maximize_window()

    top_news_elements = driver.find_elements(By.CLASS_NAME, "media__link")

    for i, news_element in enumerate(top_news_elements[:10]):
        print(f"{i + 1}. {news_element.text}")

    # Close the browser
    driver.quit()

if __name__ == '__main__':
    main()

