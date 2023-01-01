from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

site_url = "http://www.facebook.com"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver:  # we need to user service=serv_obj, but it's showing error
    driver.maximize_window()  # maximize the browser window
    driver.get(site_url)
    # tag and Class - tagname.classname - need to use . before every class name
    driver.find_element(By.CSS_SELECTOR, "input.inputtext._55r1._6luy").send_keys("hi there")
    # tag and ID - tagname.id - need to use # before id
    driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("hi there")
    # tag class and attribute - tagname.classname[attribute=value]
    print(driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=email]").send_keys("hi there"))
    # tag and attribute - tagname[attribute=value]
    driver.find_element(By.CSS_SELECTOR, "button[type=submit]").submit()
