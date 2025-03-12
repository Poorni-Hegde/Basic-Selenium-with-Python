import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

login_url = 'https://the-internet.herokuapp.com/broken_images'
driver.get (login_url)
driver.maximize_window()

images = driver.find_elements(By.TAG_NAME, value= "img")
broken_images = []

for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print("Broken Image Found")

if broken_images:
    print("List of Broken Images:")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("No Broken Images Found")

driver.close()
