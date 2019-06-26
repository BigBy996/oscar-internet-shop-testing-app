from const_storage import CartTextConsts, TestConfig
from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    def should_not_see_products_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_SUMMARY), \
            "Expected basket to be empty, but it wasn't"

    def should_see_empty_basket_text(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_BASKET_TEXT), \
            "Expected text about empty basket to be presented, but it wasn't"
        basket_text = self.browser.find_element(*CartPageLocators.EMPTY_BASKET_TEXT).text
        user_lang = TestConfig.language
        assert basket_text == CartTextConsts.CART_EMPTY_TEXT_DICT[user_lang], \
            "Expected \"{}\" to be presented, but \"{}\" found" \
                .format(CartTextConsts.CART_EMPTY_TEXT_DICT[user_lang], basket_text)
