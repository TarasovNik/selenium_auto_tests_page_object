from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no \"login\" in link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_line = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_first_line = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_second_line = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

        email_line.send_keys(email)
        password_first_line.send_keys(password)
        password_second_line.send_keys(password)
        registration_button.click()
