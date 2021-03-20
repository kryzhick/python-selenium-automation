from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_LINK = (By.ID, 'nav-orders')
    SING_IN = (By.CSS_SELECTOR, 'h1')
    EMPTY_CART = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')

    def open_main_page(self):
        self.open_url('https://www.amazon.com/')

    def input_amazon_search(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)

    def click_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def click_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def verify_sing_in_open(self, search_query):
        self.verify_text(search_query, *self.SING_IN)

    def verify_cart_is_empty(self, search_query):
        self.verify_text(search_query, *self.EMPTY_CART)

