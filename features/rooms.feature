
  Feature: Rooms Page Verification
    As a potential hotel guest
    I want to view available rooms and their details
    So that I can select and book the right room for my stay

    Background:
    Given I navigate to the Rooms page

  Scenario: Verify page title
    Then the rooms page title should be "Our Rooms"

  Scenario: Verify rooms subtitle
    Then the rooms subtitle should be "Comfortable beds and delightful breakfast from locally sourced ingredients"

  Scenario: Verify all three room images are displayed
    Then all three room images should be displayed


  Scenario: Verify room titles
    Then the room titles should be:
      | Single |
      | Double |
      | Suite  |

  Scenario: Verify all rooms have description
    Then all rooms should have descriptions displayed

  Scenario: Verify all rooms have features displayed
    Then all rooms should have features displayed

  Scenario: Verify room prices
    Then the room prices should be:
      | £100 per night |
      | £150 per night |
      | £225 per night |


  Scenario Outline: Booking different room type
    When I click Book Now for the "<room_type>" room
    Then I should be redirected to the reservation page
    And I should be on the reservation page for room "<room_id>"

    Examples:
      | room_type | room_id |
      | Single    | 1       |
      | Double    | 2       |
      | Suite     | 3       |

