import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

def calculator_session():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "12",
        "app": "C:/Users/odunuga/kehinde-testify/Downloads/Calculator_8.4 (503542421)_Apkpure.apk",
        "appPackage": "com.google.android.calculator",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)

    time.sleep(3)
    driver.get_screenshot_as_file("calculator.png")
    driver.quit()

def youtube_session():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "12",
        "appPackage": "com.google.android.apps.youtube.music",
        "appActivity": ".activities.MusicActivity",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)

    time.sleep(3)
    driver.get_screenshot_as_file("youtube_music.png")
    driver.quit()

def main():
    calculator_session()
    youtube_session()

if __name__ == '__main__':
    main()