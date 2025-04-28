import pytest

class TestContext:
    def __init__(self):
        self.login_page = None
        self.products_page = None
        self.cart_page = None
        self.checkout_page = None

@pytest.fixture
def test_context():
    return TestContext()
