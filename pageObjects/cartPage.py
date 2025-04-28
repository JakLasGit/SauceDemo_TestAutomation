from playwright.sync_api import expect
from pageObjects.checkoutPage import CheckoutPage

class CartPage:
    def __init__(self, page):
        self.page = page
        self.continue_shopping_button = page.locator("#continue-shopping")
        self.cart_item_list = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    def back_to_products_page(self):
        from pageObjects.productsPage import ProductsPage
        self.continue_shopping_button.click()
        productsPage = ProductsPage(self.page)
        return productsPage

    def remove_first_item_from_cart(self):
        self.first_item = self.cart_item_list.nth(0)
        self.first_item.get_by_role("button", name="Remove").click()

    def navigate_to_checkout(self):
        self.checkout_button.click()
        checkoutPage = CheckoutPage(self.page)
        return checkoutPage