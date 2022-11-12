import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Challenge 3

# Navigate to any browser https://www.weather.com/ get the current temperature and print it out in the terminal.
# Then print out the temperature for Morning, Afternoon, Evening, and overnighgt.


def main():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://weather.com/")
    driver.maximize_window()

    current_temperature = driver.find_element(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/span')
    print("Current Temperature:", current_temperature.text)

    morning_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[1]/a/div[1]/span')
    print("Morning Temperature:", morning_temperature.text)

    afternoon_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[2]/a/div[1]/span')
    print("Afternoon Temperature:", afternoon_temperature.text)

    evening_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[3]/a/div[1]/span')
    print("Evening Temperature:", evening_temperature.text)

    overnight_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[4]/a/div[1]/span')
    print("Overnight Temperature:", overnight_temperature.text)


    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    main()