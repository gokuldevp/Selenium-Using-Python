"""
upload file : using send keys
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

loaction = os.getcwd()
site_url = "https://www.monsterindia.com/"

def chrome_setup():
    # uploading a file
    serv_obj = Service("D:\Development\driver\Chrome\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver


driver = chrome_setup()
driver.maximize_window()
driver.get(site_url)
driver.implicitly_wait(5)


driver.find_element(By.XPATH, '//*[@id="user-signup-actions"]/div[1]/div[1]/a[2]').click()
driver.find_element(By.ID, "file-upload").send_keys("C:/Users/Gokul Dev P/OneDrive\Documents/gokul personal details/Brochure.pdf")
# driver.find_element(By.XPATH, '//*[@id="pop_upload"]').click()
driver.quit()
