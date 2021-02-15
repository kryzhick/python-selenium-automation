from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

ham_menu = (By.ID, 'nav-hamburger-menu')

@then ('Veryfy hamburger icon is visible')
def verify_menu_present(context):
    print('find element')
    element = context.driver.find_element(*ham_menu)
    print(element)
    print(type(element))

    print('find elements')
    elements = context.driver.find_elements(*ham_menu)
    print(elements)
    print(type(elements))

    context.driver.find_element(*ham_menu)

    assert len(elements) == 1
