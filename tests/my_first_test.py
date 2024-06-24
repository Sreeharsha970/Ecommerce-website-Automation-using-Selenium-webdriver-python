import time

from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://www.saucedemo.com/")
        time.sleep(5)
        self.type("#user-name", "standard_user")         # username
        self.type("#password", "secret_sauce\n")         # password
        time.sleep(5)
        self.assert_element("div.inventory_list")                    # products list
        self.assert_exact_text("Products", "span.title")       # products class is span.title
        self.click('button[name*="backpack"]')                             # backpack is the product name
        self.click("#shopping_cart_container a")
        self.assert_exact_text("Your Cart", "span.title")       # your cart inspect
        self.assert_text("Backpack", "div.cart_item")         # backpack is added to cart or not
        self.click("button#checkout")                                  # checking
        self.type("#first-name", "SeleniumBase")
        self.type("#last-name", "Automation")
        self.type("#postal-code", "12345")
        time.sleep(5)
        self.click("input#continue")
        self.assert_text("Checkout: Overview")
        self.assert_text("Backpack", "div.cart_item")        # backpack class name
        self.assert_text("29.99", "div.inventory_item_price")   # price class name
        self.click("button#finish")
        self.assert_exact_text("Thank you for your order!", "h2")
        time.sleep(5)
        self.assert_element('img[alt="Pony Express"]')
        self.js_click("a#logout_sidebar_link")
        self.assert_element("div#login_button_container")
