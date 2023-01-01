"""
Browser Commands

-> close() - close single browser window (where driver focused) - will not kill the process
-> quit() - close multiple browser windows - killing the process of the chrome driver

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

site_url = "https://demo.nopcommerce.com/register"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

# close
driver = webdriver.Chrome(service=serv_obj)  # we need to user service=serv_obj, but it's showing error
driver.maximize_window()  # maximize the browser window
driver.get(site_url)
driver.close()

# quit
driver1 = webdriver.Chrome(service=serv_obj)  # we need to user service=serv_obj, but it's showing error
driver1.maximize_window()  # maximize the browser window
driver1.get(site_url)
driver1.quit()
