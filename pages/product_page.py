from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_btn.click()
        BasePage.solve_quiz_and_get_code(self)

    def check_price(self):
        def page_price(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_PAGE).text

        def alert_price(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT).text

        assert alert_price(self) == page_price(self), "Other prices"

    def check_name(self):
        def page_name(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE).text

        def alert_name(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        assert alert_name(self) == page_name(self), "Other names"

