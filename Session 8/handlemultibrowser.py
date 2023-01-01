"""
For handling browser windows we use

driver.switch_to.window(WindowID) - where WindowID are dynamic and auto created by browser

driver.current_window_handle - Return WindowID of single browser window
driver.window_handles - Return WindowID's o multiple browser window - can use loop if there is lots of windows


driver.close() - close current window
driver.quit() - closer all window

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

site_url = "https://opensource-demo.orangehrmlive.com/"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get(site_url)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

windowid = driver.current_window_handle  # return current window id
windowids = driver.window_handles  # return all window ids

Parent_window = windowids[0]
childwindow1 = windowids[1]

print("title of parent window: ",driver.title)
driver.switch_to.window(childwindow1)
print("title of child window : ",driver.title)

# to close a specif browser window
for win in windowids:
    driver.switch_to.window(win)
    if driver.title == "OrangeHRM":
        driver.close()

# driver.quit()
