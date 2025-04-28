Feature: Shopping Cart Functionality

  Background: User is logged in and is on the products page and has something in cart
    Given User is on a login page
    And User enters valid credentials and log in
    And User adds something to the cart
    And User is on the cart page

  @cart @navigation
  Scenario: Navigate to the cart page and return to the products page
    When User clicks the 'Continue Shopping' button
    Then User should be redirected back to the products page

  @cart @smoke
  Scenario: Remove a product from the cart page
    When User clicks the 'Remove' button next to product
    Then The cart icon counter should be hidden

  @cart @checkout
  Scenario: Proceed to checkout from the cart page with items
    When User clicks the 'Checkout' button
    Then User should be redirected to the checkout information page