from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "http://automationpractice.com/index.php"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver:  # we need to user service=serv_obj, but it's showing error
    driver.maximize_window()  # maximize the browser window
    driver.get(site_url)
    sliders = driver.find_elements(By.CLASS_NAME, 'homeslider-container')
    print("Number of sliders: ", len(sliders))
    links = driver.find_elements(By.TAG_NAME, 'a')
    print("Total Number of links: ", len(links))

