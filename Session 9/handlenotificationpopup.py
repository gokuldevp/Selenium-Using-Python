"""
Handle Notification Popups -
> these are popup that not related to any web elements, we need to disable them in the browser setting its self.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")  # disable notifications at browser level.

site_url = "https://whatmylocation.com/"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.maximize_window()
driver.get(site_url)