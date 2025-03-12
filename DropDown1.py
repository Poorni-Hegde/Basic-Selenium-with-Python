"""4 concepts covered
1. How to Interact with DropDown
2. How to use Select Class
3. How to use 3 Different  Select Methods
4. Looping the Dropdown Value
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()

login_url = 'https://the-internet.herokuapp.com/dropdown'
driver.get(login_url)

dropdown_element = driver.find_element(By.ID, value= "dropdown")
select = Select(dropdown_element)

"""select the value by visible text
===========================================
select.select_by_visible_text("Option 2")"""


"""select the value by  index
===============================
select.select_by_index(1) """


""" select the value by value
=================================
#select.select_by_value("2") """

option_count = len(select.options)
expected_count = 3

if option_count == expected_count:
    print('Test Case Passed. Count is Verified')
else:
    print('Test Case Failed. Count is Mismatched')


target_value = "Option 2"
select = Select(dropdown_element)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"Option {target_value} not found")

driver.close()


