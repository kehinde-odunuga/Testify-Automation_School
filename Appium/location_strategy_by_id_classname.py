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
        "appPackage": "com.android.chrome",
        "appActivity": "com.google.android.apps.chrome.Main",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    #accept_continue_btn = driver.find_element(MobileBy.ID, "com.android.chrome:id/terms_accept")
    #chrome_btn = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@content-desc="Chrome"]')
    accept_continue_btn = driver.find_element(MobileBy.ID, "com.android.chrome:id/terms_accept")

    #chrome_btn.click()
    accept_continue_btn.click()

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()