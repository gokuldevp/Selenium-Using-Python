from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://www.countries-ofthe-world.com/flags-of-the-world.html"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get(site_url)

## 1. Scrolling down by pixel
# window.scrollBy(0,3000) - javascript initial position 0, move by 3000 pixel
driver.execute_script("window.scrollBy(0,3000)", "")  # execute_script - inside we use javascript code
# return window.pageYOffset; - return the pixel position in y-axis
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixel moved:", value)

## 2.Scrolling down until a certain element is found in the page
tg_flag = driver.find_element(By.XPATH, '//img[@alt="Flag of India"]')
driver.execute_script("arguments[0].scrollIntoView();",tg_flag)  # scroll till the target is reached

value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixel moved:", value)

## 3. Scrolling down the page until reaching the end of the page
# document.body.scrollHeight to get the pixel at end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixel moved:", value)

## 4. Scrolling up tthe page
# document.body.scrollHeight to get the pixel at end of the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixel moved:", value)

driver.quit()


