from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

site_url = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
actionChains = ActionChains(driver)
driver.get(site_url)

length = len(driver.find_elements(By.CLASS_NAME, "dragableBoxRight"))

for i in range(1, length+1):
    target_box = driver.find_element(By.ID, f'box10{i}')
    source_box = driver.find_element(By.ID, f'box{i}')

    # perform drag and drop
    actionChains.drag_and_drop(source_box,target_box).perform()
