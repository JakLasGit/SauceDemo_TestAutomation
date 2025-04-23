Feature: User Login Functionality

  @login @smoke
  Scenario: Successful user login
    Given User is on the login page
    When User enters the valid credentials
    Then User should be redirected to the products page
#
#  @login @negative
#  Scenario: Unsuccessful user login with invalid credentials
#    Given User is on the login page
#    When User enters the invalid username "<invalid_username>"
#    And User enters the invalid password "<invalid_password>"
#    And User clicks the "Login" button
#    Then User should see a login error message
#    And User should remain on the login page

  # Add other login-specific scenarios here if needed (e.g., empty fields, locked out user)