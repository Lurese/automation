

Feature: Hotel Room Booking Availability
  As a hotel guest
  I want to check room availability for specific dates
  So that I can plan my stay

  Background:
    Given I am on the room booking page for room "{room_id}" with dates "{checkin}" to "{checkout}"


  Scenario: Validate Single Room information
    When I view the room details
    Then the room title should be "Single Room"
    And the room description should contain "Aenean porttitor mauris sit amet lacinia molestie."
    And the room should include the feature "WiFi"
    And the room should include the feature "TV"
    And the room should include the feature "Safe"
    And the room policy should include "Check-in & Check-out"
    And the room policy should include "House Rules"
    And the room policy should include "No smoking"
    And the room policy should include "No parties or events"
    And the room policy should include "Pets allowed (restrictions apply)"
    And the room policy should include "Check-in: 3:00 PM - 8:00 PM"
    And the room policy should include "Check-out: By 11:00 AM"
    And the room policy should include "Early/Late: By arrangement"

  Scenario: Successful reservation with valid details
    When I enter firstname "{firstname}"
    And I enter lastname "{lastname}"
    And I enter email "{email}"
    And I enter phone "{phone}"
    When I click the reserve button
    Then the booking should be successful

  Scenario: Cancelling reservation
    When I click the cancel button
    Then the booking should be cancelled