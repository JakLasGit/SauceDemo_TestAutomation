# language: en
Feature: Checkout Process

  Background: User is logged in and has items in the cart
    Given User is logged in as "<username>" with password "<password>"
    And User has added product "<product_name_1>" to the cart # Use a representative product
    # Note: Scenarios below might need to override or add specific products if needed

  @checkout @navigation @info
  Scenario: Navigate to Checkout Information Page
    Given User is on the cart page
    When User clicks the "Checkout" button
    Then User should be redirected to the checkout information page

  @checkout @validation @negative
  Scenario Outline: Attempt to continue checkout with missing required information
    Given User has navigated to the checkout information page
    When User enters First Name "<First Name>"
    And User enters Last Name "<Last Name>"
    And User enters Postal Code "<Postal Code>"
    And User clicks the "Continue" button
    Then User should see an error message requiring "<Missing Field>"
    And User should remain on the checkout information page

    Examples:
      | First Name   | Last Name    | Postal Code   | Missing Field |
      |              | TestLastName | 12345         | First Name    |
      | TestFirstName|              | 12345         | Last Name     |
      | TestFirstName| TestLastName |               | Postal Code   |

  @checkout @summary @smoke
  Scenario: Successfully proceed to checkout summary after entering valid information
    Given User has navigated to the checkout information page
    When User enters the First Name "<first_name>"
    And User enters the Last Name "<last_name>"
    And User enters the Postal Code "<postal_code>"
    And User clicks the "Continue" button
    Then User should be redirected to the checkout summary page
    And The summary page should display product "<product_name_1>" # Check product from Background or scenario specific
    And The summary page should display the shipping information: "<first_name>", "<last_name>", "<postal_code>"

  @checkout @finish @smoke
  Scenario: Complete the order from the checkout summary page
    Given User has successfully navigated to the checkout summary page # Assumes valid info was entered previously
    When User clicks the "Finish" button
    Then User should be redirected to the order confirmation ("Thank you") page
    And The confirmation page should display a success message

  @thankyou @navigation @smoke
  Scenario: Return to the home page from the thank you page
    Given User has successfully placed an order and is on the thank you page
    When User clicks the "Back Home" button
    Then User should be redirected to the products page