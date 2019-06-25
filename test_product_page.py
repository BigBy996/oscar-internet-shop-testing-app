from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart_promo(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_see_success_message()
    page.should_be_success_message_with_product_name()
    page.should_see_new_basket_price_message()
    page.should_be_new_basket_price_with_product_price()
