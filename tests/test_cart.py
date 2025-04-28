from playwright.sync_api import Page
from pytest_bdd import scenarios, given, when, then
from pageObjects.loginPage import LoginPage
from conftest import TestContext

scenarios("../features/cart.feature")

@given("User is on a login page")
def user_on_login_page(test_context:TestContext ,page:Page):
    test_context.login_page = LoginPage(page)
    test_context.login_page.navigate()

@given("User enters valid credentials and log in")
def user_logs_in(test_context:TestContext):
    test_context.products_page = test_context.login_page.login()

@given("User adds something to the cart")
def user_adds_product_to_cart(test_context:TestContext):
    test_context.products_page.adding_first_item_to_cart()

@given("User is on the cart page")
def user_clicks_the_cart_button(test_context:TestContext):
    test_context.cart_page = test_context.products_page.navigate_to_cart_page()

@when("User clicks the 'Continue Shopping' button")
def user_clicks_continue_shopping_button(test_context:TestContext):
    test_context.cart_page.back_to_products_page()

@when("User clicks the 'Remove' button next to product")
def user_clicks_the_remove_button(test_context:TestContext):
    test_context.cart_page.remove_first_item_from_cart()

@when("User clicks the 'Checkout' button")
def user_clicks_checkout_button(test_context:TestContext):
    test_context.checkout_page = test_context.cart_page.navigate_to_checkout()

@then("User should be redirected back to the products page")
def user_should_be_on_products_page(test_context: TestContext):
    test_context.products_page.login_assertion()

@then("The cart icon counter should be hidden")
def user_check_cart_icon_hidden(test_context:TestContext):
    test_context.products_page.cart_icon_hidden()

@then("User should be redirected to the checkout information page")
def check_if_user_is_on_checkout_page(test_context:TestContext):
    test_context.checkout_page.validate_checkout_page_landing()