"""
Doc Download file
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

loaction = os.getcwd()
site_url = "https://file-examples.com/index.php/sample-documents-download/sample-doc-download/"


def chrome_setup():
    # download file in desired location
    prefs = {"download.default_directory": loaction}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", prefs)

    serv_obj = Service("D:\Development\driver\Chrome\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


def edge_setup():
    # download file in desired location
    prefs = {"download.default_directory": loaction}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", prefs)

    serv_obj = Service("D:\Development\driver\Edge\msedgedriver.exe")
    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver


def firefox_setup():
    # setting to avoid download window
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")  # ,mime type application/msword
    ops.set_preference("browser.download.manager.showWhenStarting", False)

    # download file in desired location  - not downloaded to the desired location
    ops.set_preference("browser.download.folderList", 2)  # 0:desktop, 1:default location, 2:desired location
    ops.set_preference("browser.download,dir", loaction)

    serv_obj = Service("D:\Development\driver\Firefox\geckodriver.exe")
    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver


driver = chrome_setup()
# driver = edge_setup()
# driver = firefox_setup()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(site_url)

driver.find_element(By.XPATH, '//*[@id="table-files"]/tbody/tr[1]/td[5]/a').click()
# driver.find_element(By.XPATH, '//*[@id="dismiss-button"]/div/svg').click()
driver.quit()