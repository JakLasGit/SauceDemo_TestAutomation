Feature: User Login Functionality

  @login @smoke
  Scenario: Successful user login
    Given User is on the login page
    When User enters the valid credentials
    Then User should be redirected to the products page

  @login @negative
  Scenario: Unsuccessful user login with invalid credentials
    Given User is on the login page
    When User enters the invalid credentials
    Then User should see a login error message

  @login @negative
  Scenario: Login on locked out user account
    Given User is on the login page
    When User enters the locked out user credentials
    Then User should see a login error message
