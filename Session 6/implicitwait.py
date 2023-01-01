"""
Wait Commands: Used to handle synchronization problems in web application

Type of wait commands in python selenium:
1. implicit wait
2. explicit wait

-> implicitly_wait(time):-the function is called after the driver is created.
                         -all the code below for the function will have this wait applied, when facing synchronization
                          problems.
                         -if the page load the fast, it proceeds with the next step, else wait upto the time specified.
                         -time value is default 0s, we can give time in second.
    The Advantage:
    1. Single statement
    2. The performance is not reduced

    The Disadvantage:
    1. when the element is not available in the given time we will get the exception error again.

note: in python time.sleep(time) can also be used for wait functionality -
    The Advantage:
    1. simple to use

    The Disadvantage:
    1. the performance of the script is reduced - when the element is available before the time given is that it will
       wait for the maximum time we provide.
    2. when the element is not available in the given time we will get the exception error again.

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

site_url = "https://www.google.com"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

driver = webdriver.Chrome(service=serv_obj) # we need to user service=serv_obj, but it's showing error
driver.implicitly_wait(10)  # implicit wait, will applicable for all the below code
driver.maximize_window()  # maximize the browser window
driver.get(site_url)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("selenium")
search_box.submit()  # submit work like Enter key

# sleep(3)  # reduce performance
driver.find_element(By.XPATH,'//h3[text()="Selenium"]').click()
driver.quit()
