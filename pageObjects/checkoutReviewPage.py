from playwright.sync_api import expect

from pageObjects.checkoutConfirmationPage import CheckoutConfirmationPage


class CheckoutReviewPage:
    def __init__(self, page):
        self.page = page
        self.item_price_list = page.locator(".inventory_item_price")
        self.summary_item_price = page.locator(".summary_subtotal_label")
        self.finish_button = page.locator("#finish")

    def validate_navigation(self):
        expect(self.summary_item_price).to_be_visible()

    def click_finish_button(self):
        self.finish_button.click()
        return CheckoutConfirmationPage(self.page)