"""
1. find_element()
 -> Locator matching with single web element -> return the matching web element
 -> Locator matching with multiple web element -> return the first matching web element
 -> Locator not matching any web element -> return NoSuchElementException

2. find_elements()
 -> Locator matching with single web element -> return list of web element (list contain one element)
 -> Locator matching with multiple web element -> return list of web elements (list contain one element)
 -> Locator not matching any web element -> return empty list

Note: in case of find_elements() we need to use list operation to access each element
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://demo.nopcommerce.com/register"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver:  # we need to user service=serv_obj, but it's showing error
    driver.maximize_window()  # maximize the browser window
    driver.get(site_url)

    #  find_elements()
    #  -> Locator matching with single web element
    single_eles = driver.find_elements(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/label")
    print(single_eles)

    sin_items = [ele.text for ele in single_eles]
    print(sin_items)

    # -> Locator matching with multiple web element
    mul_eles = driver.find_elements(By.CLASS_NAME, "inputs")
    print(mul_eles)

    mul_items = [ele.text for ele in mul_eles]
    print(mul_items)

    # -> Locator not matching any web element
    no_eles = driver.find_elements(By.ID, "hi_there")
    print(no_eles)

    #  find_element()
    #  -> Locator matching with single web element
    single_ele = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/label")
    print(single_ele.text)

    # -> Locator matching with multiple web element
    mul_ele = driver.find_element(By.CLASS_NAME, "inputs")
    print(mul_ele.text)

    # -> Locator not matching any web element
    no_ele = driver.find_element(By.ID, "hi_there")
    # print(no_ele)
