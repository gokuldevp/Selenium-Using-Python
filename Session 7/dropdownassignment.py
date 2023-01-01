"""Assignment: play with dropdowns"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

site_url = "https://testautomationpractice.blogspot.com/"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get(site_url)

# Dropdown speed - selecting from the options list
dd_speed = Select(driver.find_element(By.ID, "speed"))
speed_options = dd_speed.options
for elements in speed_options:
    if elements.text == "Slow":
        elements.click()
print(f"Selected Speed:", dd_speed.first_selected_option.text)

# Dropdown files - selecting using select_by_value() method
dd_files = Select(driver.find_element(By.NAME, "files"))
dd_files.select_by_value("3")
print(f"Selected File:", dd_files.first_selected_option.text)

# Dropdown number -  selecting using select_by_visible_text() method
dd_number = Select(driver.find_element(By.XPATH, '//select[@id="number"]'))
dd_number.select_by_visible_text("2")
print(f"Selected Number:", dd_number.first_selected_option.text)

# Dropdown products - selecting using select_by_index() method
dd_products = Select(driver.find_element(By.XPATH, "//select[@name='products']"))
products_count = len(dd_products.options)
dd_products.select_by_index(products_count-1)
print(f"Selected Products:", dd_products.first_selected_option.text)

# Dropdown animals -selecting using select_by_value() method
dd_animals = Select(driver.find_element(By.CSS_SELECTOR, "#animals"))
dd_animals.select_by_value("cat")
print(f"Selected Animal:", dd_animals.first_selected_option.text)

driver.quit()


