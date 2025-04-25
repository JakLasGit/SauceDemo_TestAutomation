from playwright.sync_api import Page
from pytest_bdd import scenarios, given, when, then
from pageObjects.loginPage import LoginPage
from conftest import TestContext

scenarios("../features/products.feature")

@given("User is on a login page")
def user_on_login_page(test_context:TestContext ,page:Page):
    test_context.login_page = LoginPage(page)
    test_context.login_page.navigate()

@given("User enters valid credentials and log in")
def user_logs_in(test_context:TestContext):
    test_context.products_page = test_context.login_page.login()

@when("User clicks the 'Add to cart' button for the first product")
def user_adds_product_to_cart(test_context:TestContext):
    test_context.products_page.adding_first_item_to_cart()

@when("User clicks the 'Add to cart' button for the second product")
def user_adds_second_product_to_cart(test_context:TestContext):
    test_context.products_page.adding_second_item_to_cart()

@when("User clicks the 'Remove' button on the same product")
def user_click_remove_button(test_context:TestContext):
    test_context.products_page.removing_first_item_from_cart()

@then("The cart icon should indicate one item")
def user_check_cart_icon(test_context:TestContext):
    test_context.products_page.cart_icon_validation()

@then("The cart icon should indicate two items")
def user_check_cart_icon2(test_context:TestContext):
    test_context.products_page.cart_icon_validation2()

@then("The cart icon counter should be hidden")
def user_check_cart_icon_hidden(test_context:TestContext):
    test_context.products_page.cart_icon_hidden()