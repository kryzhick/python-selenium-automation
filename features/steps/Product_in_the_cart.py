from behave import then, given, when
from selenium.webdriver.common.by import By

first_item = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-button")
CART = (By.ID, "nav-cart-count")

@when('Click on first result product')
def click_first_product (context):
    context.driver.find_element(*first_item).click()

@when('Add first result product into the cart')
def click_add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@then('Varify cart has {expected_count} item')
def verify_product_in_the_cart(context, expected_count):
   cart_count = context.driver.find_element(*CART).text
   assert expected_count == cart_count, f'Expected {expected_count} items but got {cart_count} '




