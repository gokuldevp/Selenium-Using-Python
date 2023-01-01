from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

site_url = "http://automationpractice.com/index.php"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver:  # we need to user service=serv_obj, but it's showing error
    driver.maximize_window()  # maximize the browser window
    driver.get(site_url)
    driver.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("printed")
    driver.find_element(By.XPATH, '//*[@id="searchbox"]/button').submit()
    sleep(5)