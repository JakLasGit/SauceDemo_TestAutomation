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
    And User clicks the 'Continue' button but stays on the same page
    Then User should see an error message requiring <Missing_Field>
    And User should remain on the checkout information page

    Examples:
      | First_Name   | Last_Name    | Postal_Code   | Missing_Field |
      | NULL         | TestLastName | 12345         | First Name    |
      | TestFirstName| NULL         | 12345         | Last Name     |
      | TestFirstName| TestLastName | NULL          | Postal Code   |

  @checkout @summary @smoke
  Scenario: Successfully proceed to checkout summary after entering valid information
    When User enters the First Name
    And User enters the Last Name
    And User enters the Postal Code
    And User clicks the 'Continue' button
    Then User should be redirected to the checkout summary page

  @checkout @finish @smoke
  Scenario: Complete the order from the checkout summary page and go back to Home Page
    Given User has successfully navigated from checkout information to the checkout review page
    When User clicks the 'Finish' button
    Then User should be redirected to the order confirmation ('Thank you') page with success message
    And User goes back to Home Page by pressing the 'Back Home' button
