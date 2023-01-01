"""
in case of inner iframe we need to use switch_to.frame() method inside a iframe

driver.switch_to.parent_frame() - to switch to parent frame
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

site_url = "http://demo.automationtesting.in/Frames.html"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get(site_url)

driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()

iframe = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
driver.switch_to.frame(iframe)

inneriframe = driver.find_element(By.XPATH, '//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inneriframe)

driver.find_element(By.TAG_NAME, "input").send_keys("Hi there")

driver.switch_to.parent_frame()