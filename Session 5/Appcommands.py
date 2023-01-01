"""
Application Commands:
1. Title       - Get the Title of the page
2. Current Url - Get the current url
3. Page_source - Get the page source
4. get()       - Open the application url
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

site_url = "http://automationpractice.com/index.php"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver:  # we need to user service=serv_obj, but it's showing error
    driver.maximize_window()  # maximize the browser window
    driver.get(site_url)
    print(f"Page Title: {driver.title}")  # title command gets the page title
    print(f"Current URL: {driver.current_url}")  # current_url command gets the url
    print(f"Page Source: {driver.page_source}")  # page_source command gets the page source
