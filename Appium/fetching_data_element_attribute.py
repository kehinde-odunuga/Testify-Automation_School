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
        "appPackage": "com.android.dialer",
        "appActivity": ".main.impl.MainActivity",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    add_favorite_btn = driver.find_element(MobileBy.ID, "com.android.dialer:id/empty_list_view_action")

    print("Attribute - Package:", add_favorite_btn.get_attribute("package"))
    print("Attribute - Resource ID:", add_favorite_btn.get_attribute("resource-id"))
    print("Attribute - Bounds:", add_favorite_btn.get_attribute("bounds"))


    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    main()