from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def create_email(self):
        """"create random email for registration"""
        email = 'test' + str(time.time()) + '@qa.com'
        return email

    def create_password(self):
        """"create random password for registration"""
        password = 'a' + str(time.time()) + 'B'
        return password

    def should_be_login_page(self):
        """"check that current page is login-page"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """"check that str 'login' is in current url"""
        assert 'login' in str(self.browser.current_url), "str 'login' not in url"

    def should_be_login_form(self):
        """"check that login page have login form"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        """"check that login page have register form"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self):
        """"register new user with random email and password. New user's email and password is adding to txt file """
        email = self.create_email()
        password = self.create_password()
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_password.send_keys(password)
        conf_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        conf_password.send_keys(password)
        registration_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        registration_btn.click()
        self.success_registration_message()
        with open('users_storage.txt', 'a') as users_storage:
            users_storage.write(str([email, password])+'\n')    # write email and password to txt file

    def success_registration_message(self):
        """"check that registration is success by find success message on page"""
        assert self.is_element_present(
            *LoginPageLocators.SUCCESS_REGISTRATION_ALERT), 'email was registered or wrong password'

    def authorize_user(self):
        pass
