from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

HAM_MENU = (By.ID, 'nav-hamburger-menu')

@then ('Verify hamburger icon is visible')
def verify_menu_present(context):
    e = context.driver.find_element(*HAM_MENU)
    context.driver.refresh()
    context.driver.find_element(*HAM_MENU).click()
     # e.click()




    # print(element)
    # print(type(element))
    #
    # print('find elements')
    # elements = context.driver.find_elements(*ham_menu)
    # print(elements)
    # print(type(elements))
    #
    # context.driver.find_element(*ham_menu)
    #
    # assert len(elements) == 1
