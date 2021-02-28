from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait



DOG_IMG = (By.CSS_SELECTOR, "a[href='/dogsofamazon'] img")


@when('Store original window')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)



@when('Click to open blog')
def click_on_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to the newly opened window')
def switch_to_new(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print(context.driver.window_handles)
    context.driver.switch_to.window(context.driver.window_handles[1])


@then('User can close new window and switch back to original')
def close_old_switch_to_new_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
