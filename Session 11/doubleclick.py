from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

site_url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
actionchains = ActionChains(driver)
driver.get(site_url)

driver.switch_to.frame("iframeResult")

# double click
button = driver.find_element(By.XPATH, "/html/body/button")
actionchains.double_click(button).perform()

# driver.quit()

