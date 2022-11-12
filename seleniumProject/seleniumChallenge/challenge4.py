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

    #latest_news = driver.find_element(By.TAG_NAME, "media_link")
    #print(latest_news)

    #time.sleep(10)
    #driver.close()

    news1 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[1]/div/div[2]/h3/a')
    news2 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[2]/div/div[2]/h3/a')
    news3 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[3]/div/div[2]/h3/a')
    news4 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[1]/div/div[2]/h3/a')
    news5 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[5]/div/div[2]/h3/a')
    news6 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[4]/div/div[2]/h3/a')
    news7 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[2]/div/div[2]/h3/a')
    news8 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]/div/div[2]/h3/a')
    news9 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[2]/div/div[2]/h3/a')
    news10 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[1]/div/div[2]/h3/a')

    print("News 1:", news1.text)
    print("News 2:", news2.text)
    print("News 3:", news3.text)
    print("News 4:", news4.text)
    print("News 5:", news5.text)
    print("News 6:", news6.text)
    print("News 7:", news7.text)
    print("News 8:", news8.text)
    print("News 9:", news9.text)
    print("News 10:", news10.text)

    time.sleep(5)
    driver.close()

if __name__ == '__main__':
    main()