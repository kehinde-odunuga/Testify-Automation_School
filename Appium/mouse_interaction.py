import time
from appium import webdriver
from selenium.webdriver import ActionChains
from appium.webdriver.common.mobileby import MobileBy


def main():
    desired_caps = {
       #"deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "12",
        "app": "C:/Users/odunuga/kehinde-testify/Downloads/Calculator_8.4 (503542421)_Apkpure.apk",
        "appPackage": "com.google.android.calculator",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    actions = ActionChains(driver)

    num2 = driver.find_element(MobileBy.ACCESSIBILITY_ID, "2")
    actions.move_to_element_with_offset(num2, 300, -300)
    #actions.move_to_element(num2)
    actions.click_and_hold()
    actions.release()
    actions.perform()


    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()