"""
Conditional commands

is_displayed() - check if the element is displayed return True/False
is_enabled() - check if the element is enabled return True/False
is_selected() - check if the element is enabled return True/False
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

    # is_displayed()
    search = driver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
    print("search displayed status:", search.is_displayed())

    # is_enabled()
    print("\nsearch enabled status:", search.is_enabled())

    # is_selected()

    print("\nDefault status....")
    male_rd = driver.find_element(By.ID, 'gender-male')
    female_rd = driver.find_element(By.ID, 'gender-female')
    print("Male radio button selected status:", male_rd.is_selected())
    print("Female radio button selected status:", female_rd.is_selected())

    print("\nAfter selecting the male radio button")
    male_rd.click()
    print("Male radio button selected status:", male_rd.is_selected())
    print("Female radio button selected status:", female_rd.is_selected())

    print("\nAfter selecting the female radio button")
    female_rd.click()
    print("Male radio button selected status:", male_rd.is_selected())
    print("Female radio button selected status:", female_rd.is_selected())