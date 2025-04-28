from playwright.sync_api import expect


class CheckoutInformationPage:
    def __init__(self, page):
        self.page = page
        self.checkout_title = page.locator(".title")

    def validate_checkout_page_landing(self):
        expect(self.checkout_title).to_have_text("Checkout: Your Information")