from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

login_url = 'https://cosmocode.io/automation-practice-webtable/'
driver.get(login_url)
driver.maximize_window()

driver.execute_script("window.scrollTo(0,700)")

table = driver.find_element(By.ID, value= "countries")
rows = table.find_elements(By.TAG_NAME, value= "tr")
row_count = (len(rows)-1)
print(f"Number of Rows: {row_count}")
target_value = "Australiaaa"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, value= "td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Found Value: '{target_value}'")
            found = True
            break
    if found:
        break
if not found:
    print(f"Target Value '{target_value}' is not found")