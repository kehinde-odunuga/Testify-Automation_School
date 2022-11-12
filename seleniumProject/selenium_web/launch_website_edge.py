
from selenium import webdriver


def main():
    driver = webdriver.Edge(executable_path=r"C:\Users\odunuga\Desktop\Kehinde\Web_drivers\edgedriver_win64/msedgedriver.exe")
    driver.get("http://www.google.com")
    driver.close()


main()