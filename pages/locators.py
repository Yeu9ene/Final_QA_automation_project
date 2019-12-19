from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>a")


class BasketPageLocators:
    BASKET_TITLE = (By.TAG_NAME, "h1")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class ProductPageLocators:
    PRODUCT_NAME_PAGE = (By.TAG_NAME, "h1")
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_PRICE_PAGE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_ALERT = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".basket-mini>strong")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


