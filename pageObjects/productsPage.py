from playwright.sync_api import expect
from pageObjects.cartPage import CartPage

class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.page_header = page.locator(".app_logo")
        self.product_item_list = page.locator(".inventory_item")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.shopping_cart_button = page.locator(".shopping_cart_link")

    def login_assertion(self):
        expect(self.page_header).to_contain_text("Swag Labs")

    def adding_first_item_to_cart(self):
        self.first_item = self.product_item_list.nth(0)
        self.first_item.get_by_role("button", name="Add to cart").click()

    def adding_second_item_to_cart(self):
        self.second_item = self.product_item_list.nth(1)
        self.second_item.get_by_role("button", name="Add to cart").click()

    def removing_first_item_from_cart(self):
        self.first_item = self.product_item_list.nth(0)
        self.first_item.get_by_role("button", name="Remove").click()

    def cart_icon_hidden(self):
        expect(self.shopping_cart_badge).to_be_hidden()

    def cart_icon_validation(self):
        expect(self.shopping_cart_badge).to_have_text("1")

    def cart_icon_validation2(self):
        expect(self.shopping_cart_badge).to_have_text("2")

    def navigate_to_cart_page(self):
        self.shopping_cart_button.click()
        cartPage = CartPage(self.page)
        return cartPage