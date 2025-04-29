from playwright.sync_api import expect

class CheckoutConfirmationPage:
    def __init__(self, page):
        self.page = page
        self.thankyou_message = page.locator(".complete-header")
        self.back_home_button = page.locator("#back-to-products")

    def validate_navigation(self):
        expect(self.thankyou_message).to_have_text("Thank you for your order!")

    def navigate_to_home_page(self):
        self.back_home_button.click()