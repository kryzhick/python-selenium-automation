from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

@given('Open Amazon page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com')

@when ('Click on cart icon')
def click_amazon_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()

@then('Cart is empty')
def cart_is_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    expected_text = 'Your Amazon Cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'