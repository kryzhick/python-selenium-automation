from behave import given, then, when
from selenium.webdriver.common.by import By



JEANS_COLORS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '.selection')

@given('Open Amazon {productid} page')
def open_jeans_page(context, productid):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@then('Verify user can click through colors')
def verify_can_select_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage','Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage','Vintage Light Wash', 'Washed Black']
    colors = context.driver.find_elements(*JEANS_COLORS)

    for i in range(len(colors)):
        colors[i].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[i] == selected_color, f'Expected {expected_colors[i]}, but get {selected_color}'
