import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'


@pytest.mark.need_review
def test_guest_can_go_to_login_page(browser, link=link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


def test_guest_should_see_login_link_on_product_page(browser, link=link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}" for N in
                          range(7)] +
                         [pytest.param(
                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                             marks=pytest.mark.xfail)] +
                         [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}" for N in
                          range(8, 10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_btn()
    page.check_name()
    page.check_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_btn()
    page.success_message_not_presented()


def test_guest_cant_see_success_message(browser, link=link):
    page = ProductPage(browser, link)
    page.open()
    page.success_message_not_presented()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link=link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_btn()
    page.success_message_is_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link=link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_basket_title()
    basket_page.is_basket_empty()
    basket_page.basket_is_empty_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'):
        self.browser = browser
        self.link = link
        page = ProductPage(self.browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(self.browser, url=str(self.browser.current_url))
        login_page.register_new_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_authorized_user()
        page.success_message_not_presented()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_authorized_user()
        page.add_to_basket_btn()
        page.check_name()
        page.check_price()
