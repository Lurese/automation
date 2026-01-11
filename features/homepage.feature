
 Feature: Home Page verification

   Background:
   Given I am on the home page

  Scenario: Verify home page title
    Then the title should be "Welcome to Shady Meadows B&B"

  Scenario: Verify description text
    Then the description should be correct

