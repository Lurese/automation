
  Feature: Hotel Contact Form
  As a potential guest
  I want to use the contact form to send messages
  So that I can communicate with the hotel

  Background:
    Given I am on the hotel contact page

    Scenario: Successful submission with valid contact details
      When I enter valid contact details
      And I submit the contact form
      Then the thank you message should be displayed correctly

      Scenario: Unsuccessful submission without any details
        When I submit the contact form without entering any details
        Then all alert error messages should be displayed