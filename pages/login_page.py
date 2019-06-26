from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        # достаём необходимые элементы
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        # ввод данных для регистрации
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)

        # регистрация пользователя
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url is not related to login page"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)
