import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
browser.maximize_window()

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

"""to check single checkbox
browser.find_element(By.XPATH, value= "//label[normalize-space()='Sunday']").click()
time.sleep(5)
browser.find_element(By.XPATH, value= "//label[normalize-space()='Sunday']").click()
time.sleep(5)
"""

"""to check all the checkbox"""
checkboxes = browser.find_elements(By.XPATH, value= "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1

expected_checked_count = 7

if checked_count == expected_checked_count:
    print('Checkbox Count is Verified')
else:
    print('Checkbox Count is Mismatched')
time.sleep(5)
browser.close()
