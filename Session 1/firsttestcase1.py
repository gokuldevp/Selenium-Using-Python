#  Version selenium 3
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

site_url = "https://opensource-demo.orangehrmlive.com"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"
username = "Admin"
password = "admin123"
expected_title = "OrangeHRM"

with webdriver.Chrome(executable_path=driver_path) as driver:
    driver.get(site_url)
    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_name("Submit").submit()
    title = driver.title
    if expected_title == title:
        status = "Passed"
    else:
        status = "Failed"
    print(f"Login Test {status}")

