from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def main():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("http://www.google.com")
    driver.close()


if __name__== '__main__':
    main()