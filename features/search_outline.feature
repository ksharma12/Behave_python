Feature: google search

  @smoke
  Scenario Outline: validating the search feature
    Given I navigate to google.com
    When I Validate the Page title
    Then I enter the text as "<search_title>"
    And I click the search button
    Examples:
      |search_title|
      |Hello BDD   |
      |Hello TDD   |