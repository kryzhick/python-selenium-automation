from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path='/Users/aleksandrkryzhanovskii/Automation/python-selenium-automation/chromedriver')
driver.implicitly_wait(4)
driver.get('https://www.amazon.com/gp/help/customer/display.html')

serch = driver.find_element(By.ID, 'helpsearch')
serch.send_keys('cancel order' + Keys.ENTER)


actual_text = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
expected_text = 'Cancel Items or Orders'
assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()

