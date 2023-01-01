from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site_url = "https://money.rediff.com/gainers/bse/daily/groupa"
driver_path = "D:\Development\driver\Chrome\chromedriver.exe"

serv_obj = Service(driver_path)

with webdriver.Chrome(service=serv_obj) as driver: # we need to user service=serv_obj, but it's showing error
    driver.maximize_window()
    driver.get(site_url)

    # self node
    self_text = driver.find_element(By.XPATH, "//a[normalize-space()='CARE Ratings']/self::a").text
    print("Self Test:", self_text)

    # parent node
    parent_text = driver.find_element(By.XPATH, "//a[normalize-space()='CARE Ratings']/parent::td").text
    print("\nParent Test:", parent_text)

    # ancestor node
    ancestor_text = driver.find_element(By.XPATH, "//a[normalize-space()='CARE Ratings']/ancestor::tbody").text
    print(f"\nAncestor_test:\n{ancestor_text}")

    # child nodes
    child_node = driver.find_element(By.XPATH, "//a[normalize-space()='CARE Ratings']/ancestor::tr/child::td[2]").text
    print("\nChild Test:", child_node)

    # Descendant nodes
    descendant_nodes = driver.find_elements(By.XPATH, "//a[normalize-space()='CARE "
                                                      "Ratings']/ancestor::tbody/descendant::*")
    print("\nNumber of Descendant nodes:", len(descendant_nodes))

    # Following Nodes
    following_nodes = driver.find_elements(By.XPATH, "//a[normalize-space()='CARE "
                                                     "Ratings']/ancestor::tbody/following::*")
    print("\nNumber of Following nodes:", len(following_nodes))

    # Following-sibling Nodes
    following_sibling_nodes = driver.find_elements(By.XPATH, "//a[normalize-space()='CARE "
                                                             "Ratings']/ancestor::tr/following-sibling::tr")
    print("\nNumber of Following-Sibling nodes:", len(following_sibling_nodes))

    # Preceding Nodes
    preceding_nodes = driver.find_elements(By.XPATH, "//a[normalize-space()='CARE "
                                                     "Ratings']/ancestor::tbody/preceding::*")
    print("\nNumber of Preceding Nodes:", len(preceding_nodes))

    # Preceding-sibling Nodes
    preceding_sibling_nodes = driver.find_elements(By.XPATH, "//a[normalize-space()='CARE "
                                                     "Ratings']/ancestor::tbody/preceding-sibling::*")
    print("\nNumber of Preceding-sibling Nodes:", len(preceding_sibling_nodes))