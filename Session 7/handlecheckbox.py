"""
handling checkbox

-> is_selected() - to check if the checkbox is selected or not
-> click() - to click the checkbox
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://itera-qa.azurewebsites.net/home/automation"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

driver = webdriver.Chrome(service=serv_obj)  # we need to user service=serv_obj, but it's showing error
driver.implicitly_wait(1)
driver.maximize_window()  # maximize the browser window
driver.get(site_url)

# select specific checkbox
driver.find_element(By.ID, "monday").click()
driver.find_element(By.ID, "monday").click()

# selecting multiple(without choice) check box (Which days of the week are best to start something new?)
DaysBox = driver.find_elements(By.XPATH, "//label/input[@type='checkbox']")  # can also use "//input[@type='checkbox' and contains(@id,day)]"
print("\nWithout choice:")
for day in DaysBox:
    day.click()
    print(f"is {day.get_attribute('id')} selected:", day.is_selected())

for day in DaysBox:
    day.click()

# selecting multiple(with choice) check box (Which days of the week are best to start something new?)
print("\nWith choice:")
for day in DaysBox:
    WeekName = day.get_attribute("id")
    if WeekName in ["monday", "friday", "sunday"]:
        day.click()
    print(f"is {day.get_attribute('id')} selected:", day.is_selected())

for day in DaysBox:
    WeekName = day.get_attribute("id")
    if WeekName in ["monday", "friday", "sunday"]:
        day.click()

# selecting last few check boxes(reverse order) - along with all elements
print("\nSelecting last two elements: (range)")
for i in range(len(DaysBox)-1, -1, -1):
    if i>len(DaysBox)-3:
        DaysBox[i].click()
    print(f'is {DaysBox[i].get_attribute("id")} selected:', DaysBox[i].is_selected())

# selecting last few check boxes(reverse order) - with just last 2 elements alone
print("\nSelecting last two elements: (list operation))")
for day in DaysBox[-2::]:
    day.click()
    print(f"is {day.get_attribute('id')} selected:", day.is_selected())

# marking everything as selected in check boxes
print("\nTicking all check boxes:")
for day in DaysBox:
    if not day.is_selected():
        day.click()
    print(f"is {day.get_attribute('id')} selected:", day.is_selected())

# marking everything as unselected in check boxes
print("\nunselecting all check boxes:")
for day in DaysBox:
    if day.is_selected():
        day.click()
    print(f"is {day.get_attribute('id')} selected:", day.is_selected())

driver.quit()
