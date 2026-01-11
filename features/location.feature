

Feature: Hotel Location Information
  As a potential guest
  I want to view the hotel's location and contact information
  So that I can plan my visit and contact the hotel if needed

  Background:
    Given I am on the hotel location page

  Scenario: Verify page header is displayed
    Then the page header should be "Our Location"

  Scenario: Verify location description is displayed
    Then the location description should be "Find us in the beautiful Newingtonfordburyshire countryside"

  Scenario: Verify hotel address is displayed
    Then the address should be "Shady Meadows B&B, Shadows valley, Newingtonfordburyshire, Dilbery, N1 1AA"

  Scenario: Verify hotel phone number is displayed
    Then the phone number should be "012345678901"

  Scenario: Verify hotel email is displayed
    Then the email should be "fake@fakeemail.com"

  Scenario: Verify getting here text contains welcome message
    Then the getting here section should contain "Welcome to Shady Meadows"



