import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "11",
        "app": "C:/Users/odunuga/kehinde-testify/Downloads/Calculator_8.4 (503542421)_Apkpure.apk",
        "appPackage": "com.google.android.calculator",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    num2 = driver.find_element(MobileBy.ACCESSIBILITY_ID, "2")
    num2.click()
    time.sleep(1)
    multiply = driver.find_element(MobileBy.ACCESSIBILITY_ID, "multiply")
    multiply.click()
    time.sleep(1)
    num5 = driver.find_element(MobileBy.ACCESSIBILITY_ID, "5")
    num5.click()
    num0 = driver.find_element(MobileBy.ACCESSIBILITY_ID, "0")
    num0.click()
    time.sleep(1)
    equal = driver.find_element(MobileBy.ACCESSIBILITY_ID, "equals")
    equal.click()

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()