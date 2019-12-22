from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_btn.click()
        BasePage.solve_quiz_and_get_code(self)

    def check_price(self):
        """"check that price in success message is equal price on page"""
        def page_price(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_PAGE).text

        def alert_price(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT).text

        assert alert_price(self) == page_price(self), "Other prices"

    def check_name(self):
        """"check that name in success message is equal name on page"""
        def page_name(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE).text

        def alert_name(self):
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        assert alert_name(self) == page_name(self), "Other names"

    def success_message_not_presented(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)