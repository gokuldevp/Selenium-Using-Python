"""
Try executing the mouse operation
1. double click
2. drag and drop
3. slider
4. scrolling

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

site_url = "https://testautomationpractice.blogspot.com/"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get(site_url)
actionChains = ActionChains(driver)

## double click
doubleBtn = driver.find_element(By.XPATH, '//button[@ondblclick="myFunction1()"]')
actionChains.double_click(doubleBtn).perform()

## drag and drop
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
actionChains.drag_and_drop(source, target).perform()

## drag and drop images
gallery = driver.find_element(By.ID, "gallery")
trash = driver.find_element(By.ID, "trash")
images = driver.find_elements(By.XPATH, '//ul[@id="gallery"]/li')

# adding images from gallery to the trash.
for img in images:
    actionChains.drag_and_drop(img, trash).perform()

# adding images from trash to gallery.
for img in images:
    actionChains.drag_and_drop(img, gallery).perform()

## slider


# driver.quit()