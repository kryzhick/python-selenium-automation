from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_result(self, result_word):
        self.verify_text(result_word, *self.RESULT)

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'Dress'