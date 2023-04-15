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
    print("Text:", add_favorite_btn.text)
    print("Size:", add_favorite_btn.size)
    print("Name:", add_favorite_btn.tag_name)
    print("Location:", add_favorite_btn.location)
    print("Location-in-view:", add_favorite_btn.location_in_view)
    print("Rectangle:", add_favorite_btn.rect)
    print("Is Selected:", add_favorite_btn.is_selected())
    print("Is Displayed:", add_favorite_btn.is_displayed())
    print("Is Enabled:", add_favorite_btn.is_enabled())

    contacts_btn = driver.find_element(MobileBy.ID, "com.android.dialer:id/contacts_tab")
    print("\n\nText:", contacts_btn.text)
    print("Size:", contacts_btn.size)
    print("Name:", contacts_btn.tag_name)
    print("Location:", contacts_btn.location)
    print("Location-in-view:", contacts_btn.location_in_view)
    print("Rectangle:", contacts_btn.rect)
    print("Is Selected:", contacts_btn.is_selected())
    print("Is Displayed:", contacts_btn.is_displayed())
    print("Is Enabled:", contacts_btn.is_enabled())

    create_new_contact = driver.find_element(MobileBy.ID, "com.android.dialer:id/empty_list_view_action")
    print("\n\nText:", create_new_contact.text)
    print("Size:", create_new_contact.size)
    print("Name:", create_new_contact.tag_name)
    print("Location:", create_new_contact.location)
    print("Location-in-view:", create_new_contact.location_in_view)
    print("Rectangle:", create_new_contact.rect)
    print("Is Selected:", create_new_contact.is_selected())
    print("Is Displayed:", create_new_contact.is_displayed())
    print("Is Enabled:", create_new_contact.is_enabled())

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()