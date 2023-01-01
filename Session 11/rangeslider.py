from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

site_url = "https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
actionChains = ActionChains(driver)
driver.get(site_url)

min_sli = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[1]')
max_sli = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[2]')

print(f"Before moving: \nMinimum slider location {min_sli.location}\nMaximum slider location {max_sli.location}")

# moving the minimum slider
actionChains.drag_and_drop_by_offset(min_sli, 100, 0).perform()

# moving the maximum slider
actionChains.drag_and_drop_by_offset(max_sli, -500, 0).perform()

print(f"After moving: \nMinimum slider location {min_sli.location}\nMaximum slider location {max_sli.location}")