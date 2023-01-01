"""
Broken Link - link that doesn't have any target page(page return response code "more >= 400" eg: 503 error)


-> We usually use LINK_TEXT or PARTIAL_LINK_TEXT as locator for links

function used:
-> click() - to click the link
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests


def deadlink_check(link):
    """Check if the link is a deadlink"""
    global nbl_count
    try:
        res = requests.head(link)
        if res.status_code >= 400:
            return True
        nbl_count += 1
        return False
    except:
        return True


site_url = "http://www.deadlinkcity.com/"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

driver = webdriver.Chrome(service=serv_obj)  # we need to user service=serv_obj, but it's showing error
driver.maximize_window()
driver.get(site_url)

total_links = driver.find_elements(By.TAG_NAME, "a")
link_count = len(total_links)
nbl_count = 0

links_detail = {}
for i in range(link_count):
    link = total_links[i].get_attribute('href')
    link_detail = {"link_test": total_links[i].text,
                   "link": link,
                   "is broken link": deadlink_check(f"{link}")}
    links_detail[f"link {i + 1}"] = link_detail

driver.quit()

# print(links_detail)
for link in links_detail:
    print(link, links_detail[link].values())

link_type_count = {"Total Links:": link_count, "Broken Links:": link_count - nbl_count, "Non Broken Links:": nbl_count}
print(link_type_count)


