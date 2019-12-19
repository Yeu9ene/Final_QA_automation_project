from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # check 'login' in url
        assert 'login' in str(self.browser.current_url), "str 'login' not in url"

    def should_be_login_form(self):
        # check login form on page
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # check registration form on page
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not present"

    def register_new_user(self):
        #e-mail =
        pass

    def authorize_user(self):
        pass
