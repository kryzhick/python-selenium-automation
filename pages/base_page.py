from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()
    def wait_until_element_dissapeare(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_until_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_url(self, url,):
        self.driver.get(url)

    def verify_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text} but get {actual_text}'