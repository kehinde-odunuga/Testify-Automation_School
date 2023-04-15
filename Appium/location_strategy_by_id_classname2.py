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
    fab_btn = driver.find_element(MobileBy.ID, "com.android.dialer:id/fab")
    fab_btn.click()
    time.sleep(1)
    frame_layout = driver.find_element(MobileBy.ID, "com.android.dialer:id/dialpad")
    number_buttons = frame_layout.find_elements(MobileBy.CLASS_NAME, "android.widget.FrameLayout")
    for number_button in number_buttons:
        number_button.click()

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()