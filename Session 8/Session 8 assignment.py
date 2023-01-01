# 1. alert
# 2. search multiple window and open them
# 3. capture WindowID of every browser Windows
# 4. based on the WindowID switch to every browser windows and captured title of every window, print them
# 5. close all browser window

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"
site_url = "https://testautomationpractice.blogspot.com/"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get(site_url)

#================================================= ALERT ==============================================================#
# alert Accept
alertbutton = driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button')
alertbutton.click()
alertwindow = driver.switch_to.alert
alertwindow.accept()

# alert dismiss
alertbutton.click()
alertwindow.dismiss()
#======================================================================================================================#

#==================================================MULTIPLE WINDOW=====================================================#
SecBox = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
SecBox.send_keys("King")
SecBox.submit()

Sec_Res = driver.find_elements(By.XPATH, '//*[@id="wikipedia-search-result-link"]/a')

windowlinks = []
for i in range(len(Sec_Res)):
    Sec_Res[i].click()
    windowlinks.append(Sec_Res[i].get_attribute("href")) # making a list of all urls of the pages

windowids = driver.window_handles  # getting windowids for multiple window

for window in windowids:
    driver.switch_to.window(window)
    title = driver.title
    print(f"\n{title}")
    if driver.current_url in windowlinks:
        print("page closed")
        driver.close()

#======================================================================================================================#

#====================================================HANDLE FRAMES=====================================================#

driver.switch_to.window(windowids[0])
driver.switch_to.frame(0)
firstname = driver.find_element(By.ID, "RESULT_TextField-1")
lastname = driver.find_element(By.ID, "RESULT_TextField-2")
phone = driver.find_element(By.ID, "RESULT_TextField-3")
country = driver.find_element(By.ID, "RESULT_TextField-4")
city = driver.find_element(By.ID, "RESULT_TextField-5")
email = driver.find_element(By.ID, "RESULT_TextField-6")
gender = driver.find_elements(By.XPATH, '//*[@id="q26"]/table/tbody/tr/td/label')
DaysBox = driver.find_elements(By.XPATH, '//*[@id="q15"]/table/tbody/tr/td/label')

firstname.send_keys("Gokul")
lastname.send_keys("Dev")
phone.send_keys("9343433444")
country.send_keys("india")
city.send_keys("Pattambi")
email.send_keys("abc@gmail.com")

for gen in gender:
    if gen.text == "Female":
        gen.click()
    # print(f"is {gen.text} selected:",gen.is_selected())


for day in DaysBox:
    day.click()
    # print(f"is {day.text} selected:",day.is_selected())

sleep(6)
driver.quit()




