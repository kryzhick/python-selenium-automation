from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from time import sleep

APP_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/gp/feature.html?docId=1000625601")
EXPECTED_URL = ('https://www.amazon.com/gp/feature.html?docId=1000625601')

@given("Open Amazon T&C page")
def open_amazon_tc_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")

@when('Store the original window')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Applications link')
def click_on_img(context):
    context.driver.find_element(*APP_LINK).click()


@when('Switch to newly opened window')
def switch_to_new(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print(context.driver.window_handles)
    context.driver.switch_to.window(context.driver.window_handles[1])


@then('Verify Amazon page is opened')
def verify_page_is_opened(context):
    url = context.driver.current_url
    print(url)
    assert  url == EXPECTED_URL, f'Expected {EXPECTED_URL} items but got {url}'


@then('Verify User can close new window and switch back to original')
def close_old_switch_to_new_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
