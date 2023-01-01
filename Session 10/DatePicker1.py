"""
Date Picker:
Most accept send_keys() method, but not all. in this case we need to select value through date picker
-> different date picker need different logic to handle
> here checking two type of date picker
1. jQuery date picker

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

serv_obj = Service("D:\Development\driver\Chrome\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)

# Using Send Keys
datePicker = driver.find_element(By.ID, "datepicker")
# datePicker.send_keys("08/09/1997")

# Using datePicker element
month = "June"
year = "2023"
day = "25"
datePicker.click()  # opens date picker

# driver.find_element(By.CLASS_NAME, 'ui-datepicker-next').click()
# driver.find_element(By.CLASS_NAME, 'ui-datepicker-next').click()
# sleep(3)
#
# datePickerPrev = driver.find_element(By.CLASS_NAME, 'ui-datepicker-prev')
# datePickerPrev.click()

months = {"January": 1,
          "February": 2,
          "March": 3,
          "April": 4,
          "May": 5,
          "June": 6,
          "July": 7,
          "August": 8,
          "September": 9,
          "October": 10,
          "November": 11,
          "December": 12}

while True:
    datePickerMonth = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    datePickerYear = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
    print(datePickerMonth, datePickerYear)
    if months[month] == months[datePickerMonth] and year == datePickerYear:
        print("Target Achieved")
        break
    else:
        if year > datePickerYear:
            driver.find_element(By.CLASS_NAME, 'ui-datepicker-next').click()
        elif year < datePickerYear:
            driver.find_element(By.CLASS_NAME, 'ui-datepicker-prev').click()
        elif months[month] > months[datePickerMonth]:
            driver.find_element(By.CLASS_NAME, 'ui-datepicker-next').click()
        elif months[month] < months[datePickerMonth]:
            driver.find_element(By.CLASS_NAME, 'ui-datepicker-prev').click()

driver.find_element(By.XPATH, f"//a[@data-date='{day}']").click()

