"""
->KeyBoard Actions
1. Ctrl+A  - Select all the text.
2. Ctrl+C
3. Tab
4. Ctrl+V
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys,ActionChains

site_url = "https://text-compare.com/"
serv_obj = Service("D:\Development\driver\Chrome\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(site_url)
act = ActionChains(driver)

input1 = driver.find_element(By.ID, "inputText1")
input2 = driver.find_element(By.ID, "inputText2")

input1.send_keys("Text for testing :)")

## input1 -> Ctrl+A
act.key_down(Keys.CONTROL)  # press the Ctrl key
act.send_keys("a").perform()
act.key_up(Keys.CONTROL)  # unpressed the Ctrl key
act.perform()

# or
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

## input1 -> Ctrl+C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

## Tab
act.send_keys(Keys.TAB)

## input2 -> Ctrl+V
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

