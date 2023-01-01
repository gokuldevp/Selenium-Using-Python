"""
-> Handling Alerts(popups)
1. We use driver.switch_to.alert  --> store in a variable "eg: obj1"
2. We can enter value in alert window by using obj1.send_keys("") method
3. We can accept/ok an alert window using obj1.accept() method
4. We can cancel an alert window using obj1.dismiss() method
5. We can use abj1.text to get the

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

site_url = "https://the-internet.herokuapp.com/javascript_alerts"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get(site_url)

# Result
result = driver.find_element(By.ID, "result")

## click for JS Prompt
# ok
# normalize-space() ignore space
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
alert_window = driver.switch_to.alert
alert_window.send_keys("Hi There")
alert_window.accept()  # Click the ok button in the alert window
print(f"click for JS Prompt and click ok -> {result.text}")

# Cancel
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
alert_window = driver.switch_to.alert
alert_window.dismiss()  # Click the cancel button in the alert window
print(f"click for JS Prompt and click cancel -> {result.text}")

## click for JS Alert
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()
alert_window = driver.switch_to.alert
print(alert_window.text)  # alert text
alert_window.accept()
print(f"click for JS Alert and click ok -> {result.text}")

## Click for JS Confirm
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
alert_window = driver.switch_to.alert
alert_window.dismiss()
print(f"Click for JS Confirm and click cancel -> {result.text}")

driver.quit()
