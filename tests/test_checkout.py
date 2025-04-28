from playwright.sync_api import Page
from pytest_bdd import scenarios, given, when, then, parsers
from pageObjects.loginPage import LoginPage
from conftest import TestContext

scenarios("../features/checkout.feature")

@given("User is logged in as standard user")
def user_logs_in(test_context:TestContext ,page:Page):
    test_context.login_page = LoginPage(page)
    test_context.login_page.navigate()
    test_context.products_page = test_context.login_page.login()

@given("User has added first product to the cart and went to cart page")
def user_adds_first_item_to_cart_and_proceeds_to_cart_page(test_context:TestContext):
    test_context.products_page.adding_first_item_to_cart()
    test_context.cart_page = test_context.products_page.navigate_to_cart_page()


@given("User pressed Checkout on a Cart page")
def user_goes_to_checkout_page(test_context:TestContext):
    test_context.checkout_information_page = test_context.cart_page.navigate_to_checkout()

@when(parsers.parse("User provides First Name: {First_Name}"))
def enter_first_name(test_context:TestContext, First_Name: str):
    first_name_value = "" if First_Name == "NULL" else First_Name
    test_context.checkout_information_page.enter_first_name(first_name_value)

@when(parsers.parse("User provides Last Name: {Last_Name}"))
def enter_last_name(test_context: TestContext, Last_Name: str):
    last_name_value = "" if Last_Name == "NULL" else Last_Name
    test_context.checkout_information_page.enter_last_name(last_name_value)

@when(parsers.parse("User provides Postal Code: {Postal_Code}"))
def enter_postal_code(test_context: TestContext, Postal_Code: str):
    postal_code_value = "" if Postal_Code == "NULL" else Postal_Code
    test_context.checkout_information_page.enter_postal_code(postal_code_value)

@when(parsers.parse("User clicks the 'Continue' button"))
def click_continue_button(test_context: TestContext):
    test_context.checkout_information_page.click_continue_negative()

@then(parsers.parse("User should see an error message requiring {Missing_Field}"))
def check_error_message(test_context: TestContext, Missing_Field: str):
    test_context.checkout_information_page.check_error_message(Missing_Field)

@then("User should remain on the checkout information page")
def check_still_on_checkout_info_page(test_context: TestContext):
    test_context.checkout_information_page.validate_checkout_page_landing()