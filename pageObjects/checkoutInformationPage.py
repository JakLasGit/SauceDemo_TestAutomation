from playwright.sync_api import expect

from pageObjects.checkoutReviewPage import CheckoutReviewPage


class CheckoutInformationPage:
    def __init__(self, page):
        self.page = page
        self.checkout_title = page.locator(".title")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.cancel_button = page.locator("#cancel")
        self.continue_button = page.locator("#continue")
        self.error_message_container = page.locator("h3[data-test='error']")

    def validate_checkout_page_landing(self):
        expect(self.checkout_title).to_have_text("Checkout: Your Information")

    def enter_first_name(self, first_name: str):
        if first_name:
            self.first_name_input.fill(first_name)
        else:
            self.first_name_input.fill("")

    def enter_last_name(self, last_name: str):
        if last_name:
            self.last_name_input.fill(last_name)
        else:
            self.last_name_input.fill("")

    def enter_postal_code(self, postal_code: str):
        if postal_code:
            self.postal_code_input.fill(postal_code)
        else:
            self.postal_code_input.fill("")

    def click_continue_negative(self):
        self.continue_button.click()

    def check_error_message(self, missing_field: str):
        expected_error_text = f"Error: {missing_field} is required"
        expect(self.error_message_container).to_have_text(expected_error_text)

    def navigate_to_checkout_review_page(self):
        self.continue_button.click()
        return CheckoutReviewPage(self.page)