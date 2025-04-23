from dotenv import load_dotenv
import os

from playwright.sync_api import expect

from pageObjects.productsPage import ProductsPage

load_dotenv()

username = os.getenv("TEST_USERNAME")
password = os.getenv("TEST_PASSWORD")


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_text_box = page.locator("#user-name")
        self.password_test_box = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self):
        self.username_text_box.fill(username)
        self.password_test_box.fill(password)
        self.login_button.click()
        productsPage = ProductsPage(self.page)
        return productsPage