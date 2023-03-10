# Created by User at 3/9/2023
Feature: # Enter feature name here
  # Enter feature description here
  @Regression
  Scenario Outline: # Check Dummy Registration Page is working as expected
    Given User navigated to Landing page
    When Verify User successfully landed on home page
    Then User moved to and clicked resources option
    Then Verify User landed on Dummy Registration Page
    Then User fill "<name>" "<phone>" "<email>" "<country>" "<city>" "<username>" <password> in Dummy Registration form
    Examples:
      | name   | phone      | email         | country | city  | username | password |
      | Keshav | 9234565456 | rony@asdf.com | India   | Delhi | username | password |

