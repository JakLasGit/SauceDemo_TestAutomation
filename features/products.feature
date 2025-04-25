Feature: Product Page Functionality

  Background: User is logged in and on the products page
    Given User is on a login page
    And User enters valid credentials and log in

  @products @smoke
  Scenario: Add a single product to the cart from the products page
    When User clicks the 'Add to cart' button for the first product
    Then The cart icon should indicate one item

  @products
  Scenario: Add multiple different products to the cart
    When User clicks the 'Add to cart' button for the first product
    And User clicks the 'Add to cart' button for the second product
    Then The cart icon should indicate two items

  @products
  Scenario: Remove a product from the cart directly from the products page
    When User clicks the 'Add to cart' button for the first product
    And User clicks the 'Remove' button on the same product
    Then The cart icon counter should be hidden