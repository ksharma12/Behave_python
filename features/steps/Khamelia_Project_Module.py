import time

from behave import *

import oR
from Selenium_Operations.Element_Operations import Element_Operations

use_step_matcher("parse")


@given("User navigated to Khamelia")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.get_url("https://www.khamelia.com/")
    context.ele_ops.maximize_window()


@then("User login into the application with valid credentials")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.khamelia_login__XPATH)
    context.ele_ops.click(oR.khamelia_login__XPATH)
    print(context.ele_ops.get_window_handles())
    context.ele_ops.switch_to_window(context.ele_ops.get_window_handles()[1])


@then("User Enter Email Address in required field for Khamelia")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.khamelia_email_address_inbox__ID)
    context.ele_ops.clear(oR.khamelia_email_address_inbox__ID)
    context.ele_ops.send_keys(oR.khamelia_email_address_inbox__ID, "mohd.ubaid@logixshapers.biz")


@then("User clicked on SignIn For Khamelia")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_invisible_locator(oR.Khamelia_login_hide__ID)
    context.ele_ops.wait_until_element_present_visible(oR.khamelia_signIn_btn__ID)
    context.ele_ops.click(oR.khamelia_signIn_btn__ID)


@then("User Enter Password in required field for Khamelia")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.khamelia_password_inbox__ID)
    context.ele_ops.clear(oR.khamelia_password_inbox__ID)
    context.ele_ops.send_keys(oR.khamelia_password_inbox__ID, "Khamel1a@07")


@then("User Uncheck Keep me sign in checkbox for Khamelia")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.khamelia_keepMeSignIn_checkbox__XPATH)
    if context.ele_ops.check_element_is_selected(oR.khamelia_keepMeSignIn_checkbox__XPATH):
        context.ele_ops.click(oR.khamelia_keepMeSignIn_checkbox__XPATH)


@given("User already logged in the application")
def step_impl(context):
    context.execute_steps('''
    Given User navigated to Khamelia
    Then User login into the application with valid credentials
    Then User Enter Email Address in required field for Khamelia
    Then User Enter Password in required field for Khamelia
    Then User Uncheck Keep me sign in checkbox for Khamelia
    Then User clicked on SignIn For Khamelia
    ''')


@then("User clicked on new project")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.new_Project__ID)
    context.ele_ops.click(oR.new_Project__ID)


@then("User select BUSINESS project type")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.new_Project_Option_Business__ID)
    context.ele_ops.click(oR.new_Project_Option_Business__ID)


@then("User clicked on SOFTWARE project type")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.new_Project_Option_Software__ID)
    context.ele_ops.click(oR.new_Project_Option_Software__ID)


@then("User clicked on PRIVATE project-type")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.new_Project_Option_Private__ID)
    context.ele_ops.click(oR.new_Project_Option_Private__ID)


@then("User select waterfall project sub-type")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Waterfall__ID)
    context.ele_ops.click(oR.Waterfall__ID)


@then("User select Basic Agile project sub-type")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Basic_Agile__ID)
    context.ele_ops.click(oR.Basic_Agile__ID)


@then("User select Agile Scrum project sub-type")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Agile_Scrum__ID)
    context.ele_ops.click(oR.Agile_Scrum__ID)


@then("User clicked on CANCEL")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.BACK_CANCEL__ID)
    context.ele_ops.click(oR.BACK_CANCEL__ID)


@then("User clicked on NEXT")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.NEXT__ID)
    context.ele_ops.click(oR.NEXT__ID)


@then("User clicked on FINISH")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.FINISH__ID)
    context.ele_ops.click(oR.FINISH__ID)


@then('User enter project name "{Project_Name}"')
def step_impl(context, Project_Name):
    time.sleep(1)
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Name_inbox__ID)
    context.ele_ops.send_keys(oR.Project_Name_inbox__ID, Project_Name)


@Then('User select project type "{Project_Type}"')
def step_impl(context, Project_Type):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Type_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.Project_Type_Dropdown__XPATH, Project_Type)


@then('User select company "{company}"')
def step_impl(context, company):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Company_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.Company_Dropdown__XPATH, company)


@then('User select team "{team}"')
def step_impl(context, team):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Team_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.Team_Dropdown__XPATH, team)


@then('User select billable hour rate "{billable_hour_rate}"')
def step_impl(context, billable_hour_rate):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.User_Hour_Rate_Radio_btn__XPATH)
    context.ele_ops.scroll_to_element(oR.User_Hour_Rate_Radio_btn__XPATH).perform_after_actionChains()
    if billable_hour_rate == "User Hour Rate":
        context.ele_ops.click(oR.User_Hour_Rate_Radio_btn__XPATH)
    elif billable_hour_rate == "Task Billable Rate":
        context.ele_ops.click(oR.Task_Billable_Rate_Radio_btn__XPATH)


@then('User select project status "{project_status}"')
def step_impl(context, project_status):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Status_Dropdown__XPATH)
    context.ele_ops.scroll_to_element(oR.Project_Status_Dropdown__XPATH).perform_after_actionChains()
    context.ele_ops.select_by_visible_text(oR.Project_Status_Dropdown__XPATH, project_status)


@then('User enter description "{description}"')
def step_impl(context, description):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Description__ID)
    context.ele_ops.scroll_to_element(oR.Description__ID).perform_after_actionChains()
    context.ele_ops.send_keys(oR.Description__ID, description)
    context.ele_ops.wait_until_element_present_visible(oR.New_Task_Number__ID)
    context.ele_ops.scroll_to_element(oR.New_Task_Number__ID)


@then('User select project workflow "{project_workflow}"')
def step_impl(context, project_workflow):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Workflow_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.Project_Workflow_Dropdown__XPATH, project_workflow)


@then('User select portfolio "{portfolio}"')
def step_impl(context, portfolio):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Portfolio_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.Portfolio_Dropdown__XPATH, portfolio)


@then('User select project rating "{project_rating}"')
def step_impl(context, project_rating):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Rating_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.Project_Rating_Dropdown__XPATH, project_rating)


@then('User select project sponsor "{project_sponsor}"')
def step_impl(context, project_sponsor):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Sponsor__XPATH)
    context.ele_ops.click(oR.Project_Sponsor__XPATH)
    try:
        context.ele_ops.wait_until_element_present_visible(oR.Project_Sponsor_User__XPATH)
        context.ele_ops.click(oR.Project_Sponsor_User__XPATH)
    except:
        context.ele_ops.wait_until_element_present_visible(oR.Project_Sponsor__XPATH)
        context.ele_ops.click(oR.Project_Sponsor__XPATH)
        context.ele_ops.click(oR.Project_Sponsor__XPATH)
        context.ele_ops.wait_until_element_present_visible(oR.Project_Sponsor_User__XPATH)
        context.ele_ops.click(oR.Project_Sponsor_User__XPATH)


@then('User select project approver "{project_approver}"')
def step_impl(context, project_approver):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Approver__XPATH)
    context.ele_ops.click(oR.Project_Approver__XPATH)
    try:
        context.ele_ops.wait_until_element_present_visible(oR.Project_Approver_User__XPATH)
        context.ele_ops.scroll_to_element(oR.Project_Approver_User__XPATH)
        context.ele_ops.click(oR.Project_Approver_User__XPATH)
    except:
        context.ele_ops.wait_until_element_present_visible(oR.Project_Approver__XPATH)
        context.ele_ops.click(oR.Project_Approver__XPATH)
        context.ele_ops.click(oR.Project_Approver__XPATH)
        context.ele_ops.wait_until_element_present_visible(oR.Project_Approver_User__XPATH)
        context.ele_ops.scroll_to_element(oR.Project_Approver_User__XPATH)
        context.ele_ops.click(oR.Project_Approver_User__XPATH)


@then('User select project contact "{project_contact}"')
def step_impl(context, project_contact):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Contact__XPATH)
    context.ele_ops.click(oR.Project_Contact__XPATH)
    try:
        context.ele_ops.wait_until_element_present_visible(oR.Project_Contact_User__XPATH)
        context.ele_ops.scroll_to_element(oR.Project_Contact_User__XPATH)
        context.ele_ops.click(oR.Project_Contact_User__XPATH)
    except:
        context.ele_ops.wait_until_element_present_visible(oR.Project_Contact__XPATH)
        context.ele_ops.click(oR.Project_Contact__XPATH)
        context.ele_ops.click(oR.Project_Contact__XPATH)
        context.ele_ops.wait_until_element_present_visible(oR.Project_Contact_User__XPATH)
        context.ele_ops.scroll_to_element(oR.Project_Contact_User__XPATH)
        context.ele_ops.click(oR.Project_Contact_User__XPATH)

@then('User select default task assignee "{default_task_assignee}"')
def step_impl(context, default_task_assignee):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Default_Task_Assignee__XPATH)
    context.ele_ops.click(oR.Project_Default_Task_Assignee__XPATH)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Assignee_User__XPATH)
    context.ele_ops.scroll_to_element(oR.Project_Assignee_User__XPATH)
    context.ele_ops.click(oR.Project_Assignee_User__XPATH)


@then('User select timezone "{timezone}"')
def step_impl(context, timezone):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.TimeZone_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.TimeZone_Dropdown__XPATH, timezone)


@then('User select working days "{working_days}"')
def step_impl(context, working_days):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Working_Days_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.Working_Days_Dropdown__XPATH, working_days)


@then('User select language "{language}"')
def step_impl(context, language):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Language_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.Language_Dropdown__XPATH, language)


@then('User enter done percentage "{done_percentage}"')
def step_impl(context, done_percentage):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Percentage__XPATH)
    context.ele_ops.clear(oR.Project_Percentage__XPATH)
    context.ele_ops.send_keys(oR.Project_Percentage__XPATH, done_percentage)


@then('User select budget and billing "{budget_billing}"')
def step_impl(context, budget_billing):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Budget_Billing_Dropdown__XPATH)
    context.ele_ops.select_by_visible_text(oR.Project_Budget_Billing_Dropdown__XPATH, budget_billing)


@then('User enter project planned hours "{planned_hours}"')
def step_impl(context, planned_hours):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Planned_Hours__XPATH)
    context.ele_ops.clear(oR.Project_Planned_Hours__XPATH)
    context.ele_ops.send_keys(oR.Project_Planned_Hours__XPATH, planned_hours)


@then('User enter project planned cost "{planned_cost}"')
def step_impl(context, planned_cost):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Planned_Cost__XPATH)
    context.ele_ops.click(oR.Project_Planned_Cost__XPATH)
    context.ele_ops.clear(oR.Project_Planned_Cost__XPATH)
    context.ele_ops.send_keys(oR.Project_Planned_Cost__XPATH, planned_cost)


@then('User enter project actual hours "{actual_hours}"')
def step_impl(context, actual_hours):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Actual_Hours__XPATH)
    context.ele_ops.clear(oR.Project_Actual_Hours__XPATH)
    context.ele_ops.send_keys(oR.Project_Actual_Hours__XPATH, actual_hours)


@then('User enter project hourly rate "{hourly_rate}"')
def step_impl(context, hourly_rate):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Hourly_Rate__XPATH)
    context.ele_ops.clear(oR.Project_Hourly_Rate__XPATH)
    context.ele_ops.send_keys(oR.Project_Hourly_Rate__XPATH, hourly_rate)


@then('User enter planned material cost "{planned_material_cost}"')
def step_impl(context, planned_material_cost):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Planned_Material_Cost__ID)
    context.ele_ops.clear(oR.Project_Planned_Material_Cost__ID)
    context.ele_ops.send_keys(oR.Project_Planned_Material_Cost__ID, planned_material_cost)


@then('User enter actual material cost "{actual_material_cost}"')
def step_impl(context, actual_material_cost):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Actual_Material_Cost__ID)
    context.ele_ops.clear(oR.Project_Actual_Material_Cost__ID)
    context.ele_ops.send_keys(oR.Project_Actual_Material_Cost__ID, actual_material_cost)


@then('User select estimated start date "{estimated_start_date}"')
def step_impl(context, estimated_start_date):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Estimated_Start_Date__ID)
    context.ele_ops.wait_until_element_invisible_locator(oR.kha_overlay__ID)
    context.ele_ops.click(oR.Project_Estimated_Start_Date__ID)
    context.ele_ops.choose_date_from_jquery_calender(estimated_start_date, oR.date_picker_next__XPATH,
                                                     oR.date_picker_previous__XPATH)
    context.ele_ops.wait_until_element_present_visible(oR.information_pop_up__XPATH)
    context.ele_ops.click(oR.information_pop_up__XPATH)


@then('User select estimated end date "{estimated_end_date}"')
def step_impl(context, estimated_end_date):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Estimated_End_Date__ID)
    context.ele_ops.wait_until_element_invisible_locator(oR.kha_overlay__ID)
    context.ele_ops.click(oR.Project_Estimated_End_Date__ID)
    context.ele_ops.choose_date_from_jquery_calender(estimated_end_date, oR.date_picker_next__XPATH,
                                                     oR.date_picker_previous__XPATH)


@then("User clicked on BACK")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.BACK_CANCEL__ID)
    context.ele_ops.click(oR.BACK_CANCEL__ID)


@then("User clicked on Project Finish Button")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.FINISH__ID)
    context.ele_ops.click(oR.FINISH__ID)
    context.ele_ops.wait_until_element_invisible_locator(oR.New_Project_Creation_Div__ID)
