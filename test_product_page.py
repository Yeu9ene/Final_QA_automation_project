import time
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators


@pytest.mark.parametrize('link',
                         [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}" for N in
                          range(1)])
def test_guest_can_go_to_login_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize('link',
                         [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}" for N in
                          range(1)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_btn()
    page.check_name()
    page.check_price()

@pytest.mark.parametrize('link',
                         [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}" for N in
                          range(1)])
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_btn()
    page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ALERT)



@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}" for N in
                          range(1)])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ALERT)


@pytest.mark.parametrize('link',
                         [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}" for N in
                          range(1)])
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_btn()
    page.is_disappeared(*ProductPageLocators.PRODUCT_NAME_ALERT)


@pytest.mark.parametrize('link',
                         [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}" for N in
                          range(1)])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_basket_title()
    basket_page.is_basket_empty()
    basket_page.basket_is_empty_message()
