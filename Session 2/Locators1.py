from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://demo.nopcommerce.com"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver:  # we need to user service=serv_obj, but it's showing error
    driver.maximize_window()  # maximize the browser window
    driver.get(site_url)

    class_name = driver.find_elements(By.CLASS_NAME, "button-1")  # all elements with the CLASS and save it in a list
    tags = driver.find_elements(By.TAG_NAME, "a")  # find all TAG a and save it in an list
    print(class_name, len(class_name), tags, len(tags), sep="\n")

    driver.find_element(By.ID, 'small-searchterms').send_keys('Lenovo Thinkpad X1 Carbon Laptop')  # ID locator
    # driver.find_element(By.NAME, 'q').send_keys('Lenovo Thinkpad X1 Carbon Laptop')  # NAME locator
    driver.find_element(By.CLASS_NAME, 'button-1').submit()  # CLASS locator - find the first class with the name
    driver.find_element(By.LINK_TEXT, 'Register').click()  # LINK_TEST
    driver.find_element(By.PARTIAL_LINK_TEXT, 'log').click()  # PARTIAL_LINK_TEST


