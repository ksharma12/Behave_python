# Created by Keshav Sharma at 3/10/2023
Feature: Seo Marketing

  @chrome
  Scenario Outline: User Successfully Login Seo Application
    Given User navigated to seo marketing landing page
    Then User enter "<email>" and "<password>" in respective fields
    Then User clicked on sign In
    Then User must be successfully navigated to the Dashboard
    Examples: User Login Credentials
      | email                        | password |
      | sandeep.agarwal@khamelia.net | Pass@123 |

  Scenario Outline: User Successfully added Team in Team Master
    When User Successfully login into the application with valid credentials
    Then User navigated to Seo marketing
    Then User navigated to Team Master
    Then User clicked on Add Team Button
    Then User enter "<team_name>" in Team Name Field
    And  User Select users from user options
      | users            |
      | Santosh_Kumar    |
      | Sandeep_Aggarwal |
      | kartik_Chaudhary |
    And  User enter "<description> in Description Section"
    Then User clicked on Submit Button
    Then Verify Team Master Added Successfully "<team_name>"
    Examples: User Login and team master Credentials
      | team_name | description                |
      | Test      | This is a Test team master |

  @firefox
  Scenario Outline: User Successfully View Team in Team Master
    When User Successfully login into the application with valid credentials
    Then User navigated to Seo marketing
    Then User navigated to Team Master
    Then User click on view for corresponding "<team_name>" to view details
    Then Verify User able to view "<team_name>"
    Then Close the View Pop up
    Examples:
      | team_name |
      | Test      |

  Scenario Outline: User Successfully delete Team in Team Master
    When User Successfully login into the application with valid credentials
    Then User navigated to Seo marketing
    Then User navigated to Team Master
    Then User delete the respective team via "<team_name>"
    Then Verify User successfully deleted "<team_name>" from Team
    Examples:
      | team_name |
      | Test      |

