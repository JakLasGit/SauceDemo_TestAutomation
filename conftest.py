import pytest


class TestContext:
    def __init__(self):
        self.login_page = None
        self.products_page = None
        self.cart_page = None
        self.checkout_information_page = None
        self.checkout_review_page = None
        self.checkout_confirmation_page = None

@pytest.fixture(scope="function")
def test_context():
    return TestContext()
