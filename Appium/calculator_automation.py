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
    number1_el = driver.find_element(MobileBy.ID, "com.google.android.calculator:id/digit_1")
    number2_el = driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="2"]')
    add_el = driver.find_element(MobileBy.ID, "com.google.android.calculator:id/op_add")
    equal_el = driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="equals"]')
    number1_el.click()
    add_el.click()
    number2_el.click()
    equal_el.click()

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()