from behave import when, then, given
from selenium.webdriver.common.by import By

benefit_boxes =(By. CSS_SELECTOR, '.benefit-box' )

@given('Open Amazon Prime page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')

@then('Verify {expected_boxes} benefit boxes are displayed')
def verify_boxes(context, expected_boxes):
    actual_boxes = context.driver.find_elements(*benefit_boxes)
    assert len(actual_boxes) == int(expected_boxes), f'Expected {expected_boxes} boxes, but we see{len(actual_boxes)}'



