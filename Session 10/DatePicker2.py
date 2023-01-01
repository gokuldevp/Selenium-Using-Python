from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

serv_obj = Service("D:\Development\driver\Chrome\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.switch_to.frame(0)

month = "Aug"
year = "1999"
day = "7"

datepicker = driver.find_element(By.ID, "dob")
datepicker.click()

# selecting the month from the drop-down
month_picker_ele = driver.find_element(By.CLASS_NAME,'ui-datepicker-month')
month_picker = Select(month_picker_ele)
month_picker.select_by_visible_text(month)

# selecting the year from the drop-down
year_picker_ele = driver.find_element(By.CLASS_NAME,"ui-datepicker-year")
year_picker = Select(year_picker_ele)
year_picker.select_by_visible_text(year)

# selecting the day from the table
day_picker = driver.find_element(By.XPATH, f"//a[@data-date='{day}']")
day_picker.click()
