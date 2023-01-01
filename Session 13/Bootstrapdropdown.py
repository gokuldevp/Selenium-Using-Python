"""
Handling Bootstrap Dropdown

Note: this program won't work since the site is using select for dropdown, not the bootstrap dropdown, but the method
      will

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"


def chrome_setup():
    serv_obj = Service("D:\Development\driver\Chrome\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver


driver = chrome_setup()
driver.maximize_window()
driver.get(site_url)
driver.implicitly_wait(5)

# Bootstrap Dropdown
driver.find_element(By.ID, "select2-billing_country-container").click()
country_list = driver.find_elements(By.XPATH, "//select[@id='billing_country']/option")

for country in country_list:
    if country.text == "india":
        country.click()
        break
# driver.quit()
