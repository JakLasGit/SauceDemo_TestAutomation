Feature: Shopping Cart Functionality

  Background: User is logged in
    # Assumes a step that handles login, user might be on products page initially
    Given User is logged in as "<username>" with password "<password>"

  @cart @navigation
  Scenario: Navigate to the cart page and return to the products page
    Given User has added product "<product_name_1>" to the cart
    And User is on the products page
    When User clicks the shopping cart icon
    Then User should be redirected to the cart page
    And The cart page should display product "<product_name_1>"
    When User clicks the "Continue Shopping" button
    Then User should be redirected back to the products page

  @cart @remove @smoke
  Scenario: Remove a product from the cart page
    Given User has added product "<product_name_1>" to the cart
    And User is on the cart page # Assumes navigation to cart happened
    When User clicks the "Remove" button next to product "<product_name_1>"
    Then Product "<product_name_1>" should disappear from the cart page
    And The cart icon (if visible) should indicate "0" items
    And User should see an indication that the cart is empty (or appropriate state)

  @cart @checkout
  Scenario: Proceed to checkout from the cart page with items
    Given User has added product "<product_name_1>" to the cart
    And User is on the cart page
    When User clicks the "Checkout" button
    Then User should be redirected to the checkout information page