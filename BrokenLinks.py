import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

login_url = "https://jqueryui.com/"

driver.get (login_url)
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, value= "a")
print(f"Total Number of links on the page is: {len(all_links)}")

for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken Link: {href} (Status Code: {response.status_code})")

driver.quit()