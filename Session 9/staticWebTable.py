"""
=> WebTable
> They are of two types
1. Static web table - In these types of table, the number of rows and columns are defined
2. Dynamic web table -  In this type of table, the number of rows and columns is fixed; it depends on the data based
                        on the data the number of rows or columns may be increased or decreased.

"""
# 1) count number of rows & columns
# 2) Read specific row & column data
# 3) Read all the rows & columns data
# 4) Read data based on condition(List books name whose author is Mukesh)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

site_url = "https://testautomationpractice.blogspot.com/"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(site_url)

print("# 1) count number of rows & columns")
# 1) count number of rows & columns
numofrows = len(driver.find_elements(By.XPATH, '//table[@name="BookTable"]//tr')) # we can use * or // skip a element in xpath
numofcolumns = len(driver.find_elements(By.XPATH, '//table[@name="BookTable"]/tbody/tr/th'))
print(f"Number of rows: {numofrows}", f"Number of columns: {numofcolumns}", sep="\n")

print("\n# 2) Read specific row & column data")
# 2) Read specific row & column data
data = driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr[5]/td[1]').text
print("Book Name:", data)

print("\n# 3) Read all the rows & columns data")
# 3) Read all the rows & columns data
for i in range(2, numofrows+1):
    for j in range(1, numofcolumns+1):
        data = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr[{i}]/td[{j}]').text
        print(data, end=" | ")
    print('\n')

# 4) Read data based on condition(List books name whose author is Mukesh)
print("\n# 4) Read data based on condition(List books name whose author is Mukesh)")
author = "Mukesh"
for i in range(2, numofrows+1):
    authorname = data = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr[{i}]/td[2]').text
    if authorname == author:
        bookname = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr[{i}]/td[1]').text
        print(bookname,authorname, sep=" by ")
driver.quit()
