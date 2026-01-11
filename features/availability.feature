

  Feature: Booking Date Validation
  As a user
  I want to enter check-in and check-out dates
  So that I can check room availability

    Background:
      Given the user is on the check availability page


  Scenario: Verify default auto-filled dates
    Then the default dates should be today and tomorrow

  Scenario: Enter valid booking dates
    When the user enters check-in date "25/11/2025"
    And the user enters check-out date "26/11/2025"
    And the user clicks check availability
    Then no errors should appear

  Scenario: Enter invalid past dates
    When the user enters check-in date "01/01/2020"
    And the user enters check-out date "02/01/2020"
    And the user clicks check availability
    Then errors should appear

  Scenario: Enter non-date characters
    When the user enters check-in date "abcd"
    And the user enters check-out date "efgh"
    And the user clicks check availability
    Then errors should appear

