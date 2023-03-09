Feature: google search

  @smoke
  Scenario: validating the search feature
    Given I navigate to google.com
    When I Validate the Page title
    Then I enter the text as "Hello Behave"
    And I click the search button

  @sanity
  Scenario: validating the search feature
    Given I navigate to google.com
    When I Validate the Page title
    Then I enter the text as "Behave"
    And I click the search button