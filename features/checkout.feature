Feature: Checkout Process

  Background: User is logged in and has items in the cart
    Given User is logged in as standard user
    And User has added first product to the cart and went to cart page
    And User pressed Checkout on a Cart page

  @checkout @validation @negative
  Scenario Outline: Attempt to continue checkout with missing required information
    When User provides First Name: <First_Name>
    And User provides Last Name: <Last_Name>
    And User provides Postal Code: <Postal_Code>
    And User clicks the 'Continue' button
    Then User should see an error message requiring <Missing_Field>
    And User should remain on the checkout information page

    Examples:
      | First_Name   | Last_Name    | Postal_Code   | Missing_Field |
      | NULL         | TestLastName | 12345         | First Name    |
      | TestFirstName| NULL         | 12345         | Last Name     |
      | TestFirstName| TestLastName | NULL          | Postal Code   |

#  @checkout @summary @smoke
#  Scenario: Successfully proceed to checkout summary after entering valid information
#    Given User has navigated to the checkout information page
#    When User enters the First Name "<first_name>"
#    And User enters the Last Name "<last_name>"
#    And User enters the Postal Code "<postal_code>"
#    And User clicks the "Continue" button
#    Then User should be redirected to the checkout summary page
#    And The summary page should display product "<product_name_1>" # Check product from Background or scenario specific
#    And The summary page should display the shipping information: "<first_name>", "<last_name>", "<postal_code>"
#
#  @checkout @finish @smoke
#  Scenario: Complete the order from the checkout summary page
#    Given User has successfully navigated to the checkout summary page # Assumes valid info was entered previously
#    When User clicks the "Finish" button
#    Then User should be redirected to the order confirmation ("Thank you") page
#    And The confirmation page should display a success message
#
#  @thankyou @navigation @smoke
#  Scenario: Return to the home page from the thank you page
#    Given User has successfully placed an order and is on the thank you page
#    When User clicks the "Back Home" button
#    Then User should be redirected to the products page