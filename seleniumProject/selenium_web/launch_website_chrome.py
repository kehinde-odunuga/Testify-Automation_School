
from selenium import webdriver


def main():
    driver = webdriver.Chrome(executable_path=r"C:\Users\odunuga\Desktop\Kehinde\Web_drivers\chromedriver_win32/chromedriver.exe")
    driver.get("http://www.google.com")
    driver.close()


main()