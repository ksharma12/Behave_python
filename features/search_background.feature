Feature: google search

  Background:
    Given I navigate to google.com

  @smoke
  Scenario: validating the search feature
    When I Validate the Page title
    Then I enter the text as "Hello Behave"
    And I click the search button

  @sanity
  Scenario: validating the search feature
    When I Validate the Page title
    Then I enter the text as "Behave"
    And I click the search button