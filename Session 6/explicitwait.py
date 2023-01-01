"""
-> explicit wait:- work based on conduction's - EC - expected_conditions
                 - WebDriverWait(driver, time)
                 - we need to declare the WebDriverWait class
                 - don't need to use find element to find elements
                 - can handle exceptions
   The advantages:
   1. More effectively works
   2. Handle exceptions

   The Disadvantages:
   1. Need to use multiple places
   2. more difficult to user
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

site_url = "https://www.google.com"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

driver = webdriver.Chrome(service=serv_obj)  # we need to user service=serv_obj, but it's showing error

# MyWait = WebDriverWait(driver, 10)  # declaration of explicit wait. # basic, 10 is the maximum time waited

# Exception handling, using just Exception in list handle all exceptions
# pool_frequency - interval in which the function check the condition, 2 means the check the condition every 2 seconds
MyWait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException, Exception])


driver.maximize_window()  # maximize the browser window
driver.get(site_url)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("selenium")
search_box.submit()  # submit work like Enter key

selelink = MyWait.until(EC.presence_of_element_located((By.XPATH, '//h3[text()="Selenium"]')))  # check if the element is present
selelink.click()
driver.quit()

