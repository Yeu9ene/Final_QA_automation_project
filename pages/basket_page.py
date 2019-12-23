from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_title()

    def should_be_basket_url(self):
        # check 'login' in url
        assert 'basket' in str(self.browser.current_url), "str 'basket' not in url"

    def should_be_basket_title(self):
        # check 'login' in url
        assert self.is_element_present(*BasketPageLocators.BASKET_TITLE), "Basket title is not present"

    def basket_is_empty_message(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((BasketPageLocators.EMPTY_MESSAGE)))
        except TimeoutException:
            return False
        return True

    def is_basket_empty(self):
        try:
            WebDriverWait(self.browser, timeout=4).until(
                EC.presence_of_element_located((BasketPageLocators.PRODUCTS_IN_BASKET)))
        except TimeoutException:
            return True
        return False

