from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when ('Input Cancel order into search Help librarty field and hit ENTER')
def input_amazon_help_search(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('cancel order', Keys.ENTER)

@then('Cancel Items or Orders text is shown')
def cancel_item_or_order(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
    expected_text = 'Cancel Items or Orders'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    
