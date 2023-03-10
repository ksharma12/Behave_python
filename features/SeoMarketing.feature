# Created by Keshav Sharma at 3/10/2023
Feature: Seo Marketing


  Scenario Outline: User Successfully Login Seo Application
    Given User navigated to seo marketing landing page
    Then User enter "<email>" and "<password>" in respective fields
    Then User clicked on sign In
    Then User must be successfully navigated to the Dashboard
    Examples: User Login Credentials
      | email                        | password |
      | sandeep.agarwal@khamelia.net | Pass@123 |


  Scenario Outline: User Successfully added Team in Team Master
    Given User navigated to seo marketing landing page
    Then User enter "<email>" and "<password>" in respective fields
    Then User clicked on sign In
    Then User must be successfully navigated to the Dashboard
    Then User navigated to Seo marketing
    Then User navigated to Team Master
    Then User clicked on Add Team Button
    Then User enter "<Team_name>" in Team Name Field
    And  User Select "<User>" from user options
    And  User enter "<Description> in Description Section"
    Then User clicked on Submit Button
    Then Verify Team Master Added Successfully "<Team_name>"
    Examples: User Login and team master Credentials
      | email                        | password | Team_name | User          | Description                |
      | sandeep.agarwal@khamelia.net | Pass@123 | Test      | Santosh_Kumar | This is a Test team master |


  Scenario Outline: User Successfully delete Team in Team Master
    Given User navigated to seo marketing landing page
    Then User enter "<email>" and "<password>" in respective fields
    Then User clicked on sign In
    Then User must be successfully navigated to the Dashboard
    Then User navigated to Seo marketing
    Then User navigated to Team Master
    Then User delete the respective team via "<Team_name>"
    Then Verify User successfully deleted "<Team_name>" from Team
    Examples:
      | email                        | password | Team_name |
      | sandeep.agarwal@khamelia.net | Pass@123 | Test      |
