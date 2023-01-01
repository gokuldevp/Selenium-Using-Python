"""
Authentication popups (popup asking for username/password for signin)
-> Here we need to inject username and password in url.

syntax: https://username:password@url
eg: https://admin:admin@the-internet.herokuapp.com/basic_auth

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"
site_url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get(site_url)

body = driver.find_element(By.XPATH, '/html/body')
if "Basic Auth" in body.text:
    print("Authorised User")
else:
    print("Unauthorised user")
driver.quit()