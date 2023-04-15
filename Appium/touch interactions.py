import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def skip_page(driver):
    skip_btn = driver.find_element(MobileBy.XPATH,
                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button')

    skip_btn.click()

def touch_interaction_tap(driver):
    time.sleep(2)
    location_btn = driver.find_element(MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="Re-center map to your location"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ImageView')
    actions = TouchAction(driver)
    actions.tap(location_btn)
    actions.perform()

def touch_interaction_double_tap(driver):
    time.sleep(2)
    map_view = driver.find_element(MobileBy.ID, 'com.google.android.apps.maps:id/explore_tab_home_bottom_sheet')
    actions = TouchAction(driver)
    actions.tap(map_view)
    actions.tap(map_view)
    actions.perform()

def touch_interaction_scroll(driver):
    time.sleep(2)
    map_view = driver.find_element(MobileBy.ID, 'com.google.android.apps.maps:id/explore_tab_home_bottom_sheet')
    actions = TouchAction(driver)
    actions.press(map_view, 500, 500, 1)
    actions.move_to(map_view, 1200, 2200)
    actions.release()
    actions.perform()


def main():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "11",
        "appPackage": "com.google.android.apps.maps",
        "appActivity": "com.google.android.maps.MapsActivity",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    #skip_page(driver)
    #touch_interaction_tap(driver)
    #touch_interaction_double_tap(driver)
    touch_interaction_scroll(driver)


    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()