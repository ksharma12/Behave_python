# Created by Keshav Sharma at 3/14/2023
Feature: # In Project Creating New Tasks with variety of Options
  # Enter feature description here
  @chrome
  Scenario: User Successfully login into Khamelia
    Given User navigated to Khamelia
    Then User login into the application with valid credentials
    Then User Enter Email Address in required field for Khamelia
    Then User Enter Password in required field for Khamelia
    Then User Uncheck Keep me sign in checkbox for Khamelia
    Then User clicked on SignIn For Khamelia

  @chrome
  Scenario Outline: User Create a new business waterfall project
    Given User already logged in the application
    Then User clicked on new project
    Then User select BUSINESS project type
    Then User select waterfall project sub-type
    Then User clicked on NEXT
    Then User enter project name "<Project_Name>"
    Then User select project type "<Project_Type>"
    Then User select company "<company>"
    Then User select team "<team>"
    Then User select billable hour rate "<billable_hour_rate>"
    Then User select project status "<project_status>"
    Then User enter description "<description>"
    Then User clicked on NEXT
    Then User select project workflow "<project_workflow>"
    Then User select portfolio "<portfolio>"
    Then User select project rating "<project_rating>"
    Then User select project sponsor "<project_sponsor>"
    Then User select project approver "<project_approver>"
    Then User select project contact "<project_contact>"
    Then User select default task assignee "<default_task_assignee>"
    Then User select timezone "<timezone>"
    Then User select working days "<working_days>"
    Then User select language "<language>"
    Then User enter done percentage "<done_percentage>"
    Then User clicked on NEXT
    Then User select budget and billing "<budget_billing>"
    Then User enter project planned hours "<planned_hours>"
    Then User enter project planned cost "<planned_cost>"
    Then User enter project actual hours "<actual_hours>"
    Then User enter project hourly rate "<hourly_rate>"
    Then User enter planned material cost "<planned_material_cost>"
    Then User enter actual material cost "<actual_material_cost>"
    Then User select estimated start date "<estimated_start_date>"
    Then User select estimated end date "<estimated_end_date>"
    Then User clicked on Project Submit Button

    Examples:
      | Project_Name | Project_Type | company       | team                 | billable_hour_rate | project_status | description                 | project_workflow   | portfolio   | project_rating | project_sponsor | project_approver | project_contact | default_task_assignee | timezone              | working_days           | language     | done_percentage | budget_billing   | planned_hours | planned_cost | actual_hours | hourly_rate | planned_material_cost | actual_material_cost | estimated_start_date | estimated_end_date |
      | Test_3       | Waterfall    | Khamelia-Test | Khamelia-Test Team 1 | User Hour Rate     | Testing        | This is example description | Waterfall Workflow | Portfolio 1 | Satisfactory   | Mohd Ubaid      | Mohd Ubaid       | Mohd Ubaid      | Mohd Ubaid            | Pacific Standard Time | Mon thru Fri, plus Sat | English (UK) | 23              | Time & Materials | 500           | 3,400,000    | 600          | 500         | 4500000               | 5000000              | 05/17/2023           | 07/23/2023         |