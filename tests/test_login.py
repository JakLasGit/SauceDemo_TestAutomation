from playwright.sync_api import Page
from pytest_bdd import scenarios, given, when, then
from pageObjects.loginPage import LoginPage
from conftest import TestContext

scenarios("../features/login.feature")


#  Scenario: Successful user login
@given("User is on the login page")
def user_on_login_page(test_context:TestContext ,page:Page):
    test_context.login_page = LoginPage(page)
    test_context.login_page.navigate()

@when("User enters the valid credentials")
def user_enters_credentials(test_context:TestContext):
    test_context.products_page = test_context.login_page.login()

@then("User should be redirected to the products page")
def user_should_be_on_products_page(test_context: TestContext):
    test_context.products_page.validateLogin()