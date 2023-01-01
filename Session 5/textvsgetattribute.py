"""
Text vs GetAttribute - access through web element

-> text            - Returns inner text of the element if it's available else nothing

-> get_attribute() - Return the values(value, id, email ...) of any attribute of web element if it's available
                    else return none

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://admin-demo.nopcommerce.com/login"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver:  # we need to user service=serv_obj, but it's showing error
    driver.maximize_window()  # maximize the browser window
    driver.get(site_url)

    email = driver.find_element(By.XPATH, "//input[@id='Email']")
    email.clear()
    email.send_keys("abc@gmail.com")

    print(f"result of text: {email.text}")
    print(f"result of get_attribute('value'): {email.get_attribute('value')}")
    print(f"result of get_attribute('class'): {email.get_attribute('class')}")
