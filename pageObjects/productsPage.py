from dotenv import load_dotenv
import os

from playwright.sync_api import expect

load_dotenv()

username = os.getenv("TEST_USERNAME")
password = os.getenv("TEST_PASSWORD")

class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.page_header = page.locator(".app_logo")

    def validateLogin(self):
        expect(self.page_header).to_contain_text("Swag Labs")