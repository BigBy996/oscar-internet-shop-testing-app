from selenium.webdriver.common.by import By


class BasePageLocators(object):
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn-default[href$='/basket/']")
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class CartPageLocators(object):
    BASKET_SUMMARY = (By.ID, "basket_formset")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class MainPageLocators(object):
    LOGIN_LINK = (By.ID, "registration_link")


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")
    BASKET_NEW_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info p:nth-child(1) strong")
