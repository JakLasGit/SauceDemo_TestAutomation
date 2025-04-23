Feature: Product Page Functionality

  Background: User is logged in and on the products page
    # This assumes a step definition that logs the user in and navigates them
    # or you can make these explicit Given steps if preferred
    Given User is logged in as "<username>" with password "<password>"
    And User is on the products page

  @products @cart @smoke
  Scenario: Add a single product to the cart from the products page
    When User clicks the "Add to cart" button for product "<product_name_1>"
    Then The cart icon should indicate "1" item
    # Optional: check if the button text changed to "Remove"
    # Then The button for product "<product_name_1>" should change to "Remove"

  @products @cart
  Scenario: Add multiple different products to the cart
    When User clicks the "Add to cart" button for product "<product_name_1>"
    And User clicks the "Add to cart" button for product "<product_name_2>"
    Then The cart icon should indicate "2" items

  @products @cart
  Scenario: Remove a product from the cart directly from the products page (if possible)
    # This scenario assumes a 'Remove' button appears on the product page after adding
    Given User has added product "<product_name_1>" to the cart via the products page
    When User clicks the "Remove" button for product "<product_name_1>" on the products page
    Then The cart icon should indicate "0" items
    # Optional: check if the button text changed back to "Add to cart"
    # Then The button for product "<product_name_1>" should change to "Add to cart"