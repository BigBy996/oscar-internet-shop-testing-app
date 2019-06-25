import math
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_see_success_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ADDED_MESSAGE), \
            "Success message is not presented"

    def should_be_success_message_with_product_name(self):
        success_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADDED_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == success_message, \
            "Product name in success message \"{}\" is not equal to product name \"{}\"".format(success_message, product_name)

    def should_see_new_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_NEW_PRICE_MESSAGE), \
            "New basket price message is not presented"

    def should_be_new_basket_price_with_product_price(self):
        basket_message = self.browser.find_element(*ProductPageLocators.BASKET_NEW_PRICE_MESSAGE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == basket_message, \
            "Product price \"{}\" is not equal to updated basket price message \"{}\"".format(product_price, basket_message)

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
