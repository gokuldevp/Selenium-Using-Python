"""
Navigational commands - made in driver instance
1. back() - navigate to previous page
2. forward() - navigate to next page
3. refresh() - refresh page
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

site_url1 = "https://www.amazon.com"
site_url2 = "https://www.google.com"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver:  # we need to user service=serv_obj, but it's showing error
    driver.maximize_window()  # maximize the browser window
    driver.get(site_url1)
    driver.get(site_url2)

    # back()
    sleep(2)
    driver.back()

    # forward()
    sleep(2)
    driver.forward()

    # refresh()
    sleep(2)
    driver.refresh()

