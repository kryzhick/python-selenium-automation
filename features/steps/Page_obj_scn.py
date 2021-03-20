from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
   context.app.main_page.open_main_page()


@when('Click Amazon Orders link')
def click_orders_link(context):
    context.app.main_page.click_orders_link()


@then('Verify {search_query} page is opened')
def verify_sing_in_open(context, search_query):
    context.app.main_page.verify_sing_in_open(search_query)

@then('Verify {search_query} text present')
def verify_cart_is_empty(context, search_query):
    context.app.main_page.verify_cart_is_empty(search_query)


