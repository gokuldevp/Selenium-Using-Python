"""
Handling Dropdown
-> The tag name of Dropdown is <select> which contains multiple tag name <option> in side it.
-> Select(locator) class is used to create a select object(eg: obj)

-> The method for selecting the dropdown value from the dropdown
1. obj.select_by_visible_text("text") - text is a custom value given than can be in the dropdown
2. obj.select_by_value("value") -  the value of the attribute named value
3. obj.select_by_index(index) - Index we need to give manually(0 to n-1, where n is the number of elements)

-> to get the value of all the options
1.obj.options - return all the options as WebElement

-> to get the current select option
1. obj.first_selected_option.text

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

site_url = "https://www.opencart.com/index.php?route=account/register"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

driver = webdriver.Chrome(service=serv_obj)  # we need to user service=serv_obj, but it's showing error
driver.maximize_window()
driver.get(site_url)

drp_country_ele = driver.find_element(By.ID, "input-country")
drp_country = Select(drp_country_ele)

# select option from the dropdown using text
drp_country.select_by_visible_text("China")
print("Selected option:", drp_country.first_selected_option.text)

# select option from the dropdown using value
drp_country.select_by_value("3")
print("Selected option:", drp_country.first_selected_option.text)

# select option from the dropdown using index
drp_country.select_by_index(13)
print("Selected option:", drp_country.first_selected_option.text)

# capture all the option and print them
print(f"\nNumber of Option: {len(drp_country.options)}")
print(f"Options: \n{[option.text for option in drp_country.options]}\n")

# select option from dropdown without build-in function
for option in drp_country.options:
    if option.text == "India":
        option.click()
        break
        
print("Selected option:", drp_country.first_selected_option.text)

driver.quit()
