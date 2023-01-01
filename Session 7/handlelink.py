"""
Links:
1. Internal Link - navigate from one page of the website to another page of the same website(response code<400)
2. External Link - navigate one page of the website to another page of the different website(response code<400)
3. Broken Link - link that doesn't have any target page(page return response code "more >= 400" eg: 503 error)


-> We usually use LINK_TEXT or PARTIAL_LINK_TEXT as locator for links

function used:
-> click() - to click the link
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://demo.nopcommerce.com/"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

driver = webdriver.Chrome(service=serv_obj)  # we need to user service=serv_obj, but it's showing error
driver.maximize_window()
driver.get(site_url)

# selecting links using link text
LidoLink = driver.find_element(By.LINK_TEXT, "Digital downloads")

# selecting links using partial link text
DidoPLink = driver.find_element(By.PARTIAL_LINK_TEXT, "Digital")

# clicking the link
DidoPLink.click()

# Find the total number of links
driver.back()  # going back to home page
total_links = driver.find_elements(By.TAG_NAME, "a")
link_count = len(total_links)
print(f"Total number of links: {link_count}")

# printing all the link names, along with links as tuple in list
link_names = [(link.text, link.get_attribute("href")) for link in total_links]
print(link_names)

# printing all the link names, along with links in dictionary
links_detail = {}
for i in range(link_count):
    link_detail = {"link_test": total_links[i].text,
                   "link": total_links[i].get_attribute("href")}
    links_detail[f"link {i + 1}"] = link_detail
print(links_detail)

driver.quit()
