from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


site_url = "https://opensource-demo.orangehrmlive.com"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"
username = "Admin"
password = "admin123"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get(site_url)

#Login
driver.find_element(By.ID, "txtUsername").send_keys(username)
driver.find_element(By.ID, "txtPassword").send_keys(password)
driver.find_element(By.NAME, "Submit").click()

#Admin -> user management -> users
admin = driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]/b')
userManagement = driver.find_element(By.ID, 'menu_admin_UserManagement')
users = driver.find_element(By.ID, 'menu_admin_viewSystemUsers')

##Mousehover
actionchains = ActionChains(driver)
actionchains.move_to_element(admin).move_to_element(userManagement).move_to_element(users).perform()

# driver.quit()


