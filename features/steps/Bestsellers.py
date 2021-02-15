from behave import given, then
from selenium.webdriver.common.by import By

TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')

@given ('Open Amazon Bestsellers')
def open_amazon_bestsellers(cottext):
    cottext.driver.get('https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bsms_tab')

@Then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    assert len(actual_links) == int(expected_links), f'Expected {expected_links}, but get {len(actual_links)}'
