from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://swisnl.github.io/jQuery-contextMenu/demo.html"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get(site_url)

button = driver.find_element(By.CSS_SELECTOR, "span.context-menu-one.btn.btn-neutral")

#right click
actionchains = ActionChains(driver)
actionchains.context_click(button).perform()
