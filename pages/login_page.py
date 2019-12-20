from .base_page import BasePage
from .locators import LoginPageLocators
import time



class LoginPage(BasePage):
    def create_email(self):
        email = 'test' + str(time.time()) +'@qa.com'
        return email

    def create_password(self):
        password = '1234qwer'
        return password

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
        email = self.create_email()
        password = self.create_password()
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_password.send_keys(password)
        conf_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        conf_password.send_keys(password)


    def authorize_user(self):
        pass
