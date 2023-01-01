"""
Frame - Frame is a HTML tag that is used for dividing the web page into various frames/windows. Used as <frame> tag,
it specifies each frame within a frameset tag.

Iframe - Iframe as <iframe> is also a tag used in HTML, but it specifies an inline frame, that means it is used to
embed some other document within the current HTML document.

Frame/Iframe can be 3rd party websites


-> how to switch to frame
1. driver.switch_to.frame("frame reference")       -> selenium 4 syntax

frame reference = name of the frame, ID of the frame, webelement, index of the frame(0 in case only one frame)

tags - frame, iframe, form represents frame
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

site_url = "https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html"
chrome_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(chrome_path)

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get(site_url)

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()  # go back to main page

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()  # go back to main page

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()

driver.quit()


