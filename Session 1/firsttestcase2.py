# Version selenium 4 - Not completed
"""
Test Case:
---------------------------------------------------
1. Open web browser (Chrome/firefox/Edge)
2. Open URL https://opensource-demo.orangehrmlive.com
3. Enter username (Admin)
4. Enter Password (admin123).
5. Click on Login.
6. Capture title of the home page. (Actual title)
7. Verify title of the page: OrangeHRM
8. close browser
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://opensource-demo.orangehrmlive.com"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"
username = "Admin"
password = "admin123"
expected_title = "OrangeHRM"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver:  # we need to user service=serv_obj, but it's showing error
    driver.get(site_url)
    driver.find_element(By.ID, "txtUsername").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(password)
    driver.find_element(By.NAME, "Submit").submit()
    title = driver.title
    if expected_title == title:
        status = "Passed"
    else:
        status = "Failed"
    print(f"Login Test {status}")