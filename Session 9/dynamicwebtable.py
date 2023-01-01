from selenium import webdriver
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
driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]/b').click()
driver.find_element(By.ID, 'menu_admin_UserManagement').click()
driver.find_element(By.ID, 'menu_admin_viewSystemUsers').click()

# Managing the table
noOfRows = len(driver.find_elements(By.XPATH, "//table/tbody/tr"))
# noOfColumns = len(driver.find_elements(By.XPATH, "//table/tbody/tr[1]/td"))
print("Number of rows in the table:", noOfRows)

enabled = 0
disable = 0
for i in range(1, noOfRows+1):
    status = driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[5]")
    if status.text == "Enabled":
        enabled += 1
    else:
        disable += 1
print(f"Number of Enabled: {enabled}\nNumber of Disabled: {disable}\nTotal: {enabled+disable}")

# Assignment
# Check if the user is enabled(Status) and ESS(user role) then get the user data:
slNo = 0
for i in range(1, noOfRows+1):
    status = driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[5]").text == "Enabled"
    if status:
        userRole = driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[3]").text == "ESS"
        if userRole:
            slNo += 1
            userName = driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[2]").text
            empName = driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[4]").text
            print(f"{slNo}. Username: {userName}, Employee Name: {empName}, User Role: ESS")

driver.quit()


