import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

def skip_page(driver):
    skip_btn = driver.find_element(MobileBy.XPATH,
                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button')

    skip_btn.click()

def perform_multi_actions(driver):
    time.sleep(2)
    map_view = driver.find_element(MobileBy.ID, 'com.google.android.apps.maps:id/explore_tab_home_bottom_sheet')
    touch_actions1 = TouchAction()
    touch_actions1.press(map_view, 200, 200)
    touch_actions1.move_to(map_view, 100, 300)
    touch_actions2 = TouchAction()
    touch_actions2.press(map_view, 200, 200)
    touch_actions2.move_to(map_view, -100, -300)

    multi_actions = MultiAction(driver)
    multi_actions.add(touch_actions1, touch_actions2)
    multi_actions.perform()




def main():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "12",
        "appPackage": "com.google.android.apps.maps",
        "appActivity": "com.google.android.maps.MapsActivity",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    #skip_page(driver)
    perform_multi_actions(driver)


    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()