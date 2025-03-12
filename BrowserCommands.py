import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, value= ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
driver.close()