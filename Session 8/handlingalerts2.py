from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

site_url = "https://mypage.rediff.com/login/dologin"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get(site_url)

driver.find_element(By.XPATH, '//*[@id="pass_div"]/input[3]').click()
driver.switch_to.alert.accept()
driver.quit()

