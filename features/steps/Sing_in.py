from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



SING_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")

@when ('Click Sing in from popup')
def click_sing_in_popup (context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SING_IN_POPUP_BTN))
    e.click()

@then ('Verify Sing in page opens')
def verify_sing_in_page_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),
                              f'Url {context.driver.current_url} does not includ https://www.amazon.com/ap/signi')

    # assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, \
    # f'Url {context.driver.current_url} does not includ https://www.amazon.com/ap/signi'