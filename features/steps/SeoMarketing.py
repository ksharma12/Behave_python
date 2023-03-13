import configparser
import os
import time
from behave import *
from behave import model

import oR
from Selenium_Operations.Element_Operations import Element_Operations

use_step_matcher("parse")

this_folder = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(this_folder, "../../conf.ini")
config = configparser.RawConfigParser()
res = config.read(init_file)


@given("User navigated to seo marketing landing page")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.get_url("http://seomarketing.logixportfolio.in/")
    context.ele_ops.maximize_window()
    assert context.ele_ops.get_window_title() == "Quaapps:Login"


@then('User enter "{email}" and "{password}" in respective fields')
def step_impl(context, email, password):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.email__ID)
    context.ele_ops.clear(oR.email__ID)
    context.ele_ops.send_keys(oR.email__ID, email)
    context.ele_ops.wait_until_element_present_visible(oR.password__ID)
    context.ele_ops.clear(oR.password__ID)
    context.ele_ops.send_keys(oR.password__ID, password)


@then("User clicked on sign In")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.sign_in_button__XPATH)
    context.ele_ops.click(oR.sign_in_button__XPATH)


@then("User must be successfully navigated to the Dashboard")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.dashboard_heading__XPATH)
    assert context.ele_ops.get_element_text(oR.dashboard_heading__XPATH) == "WELCOME TO DASHBOARD"
    assert "Dashboard" in context.ele_ops.get_window_current_url()


@then("User navigated to Seo marketing")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present(oR.Seo_Marketing__XPATH)
    context.ele_ops.click(oR.Seo_Marketing__XPATH)


@then("User navigated to Team Master")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Team_Master__XPATH)
    context.ele_ops.click(oR.Team_Master__XPATH)
    assert "Team_Master" in context.ele_ops.get_window_current_url()


@then("User clicked on Add Team Button")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Add_Team__XPATH)
    context.ele_ops.click(oR.Add_Team__XPATH)
    print(context.ele_ops.get_window_current_url())
    assert "ADD" in context.ele_ops.get_window_current_url()


@then('User enter "{team_name}" in Team Name Field')
def step_impl(context, team_name):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Team_Name_input__ID)
    context.ele_ops.clear(oR.Team_Name_input__ID)
    context.ele_ops.send_keys(oR.Team_Name_input__ID, team_name)


@step('User Select users from user options')
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Select_user__ID)
    context.ele_ops.click(oR.Select_user__ID)
    context.ele_ops.wait_until_elements_present(oR.Multiple_Options__XPATH)
    for row in context.table:
        print(row["users"])
        context.ele_ops.click_from_multiple_ele_text_basis(oR.Multiple_Options__XPATH, row["users"])
    context.ele_ops.click(oR.Help_Information__XPATH)


@step('User enter "{description} in Description Section"')
def step_impl(context, description):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.switch_to_frame(oR.iframe_Description__ID)
    context.ele_ops.send_keys(oR.inside_Description__XPATH, description)
    context.ele_ops.switch_to_default_content()


@then("User clicked on Submit Button")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.submit_Btn__ID)
    context.ele_ops.click(oR.submit_Btn__ID)


@then('Verify Team Master Added Successfully "{team_name}"')
def step_impl(context, team_name):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.alert__XPATH)
    context.ele_ops.click(oR.Team_Master__XPATH)
    context.ele_ops.wait_until_element_present_visible(oR.Team_Name_Search_InputField__XPATH)
    context.ele_ops.clear(oR.Team_Name_Search_InputField__XPATH)
    context.ele_ops.send_keys(oR.Team_Name_Search_InputField__XPATH, team_name)
    context.ele_ops.wait_until_elements_present(oR.Teams_list__XPATH)
    ele_texts = [ele.text for ele in context.ele_ops.find_elements(oR.Teams_list__XPATH)]
    if team_name in ele_texts:
        assert True
    elif team_name not in ele_texts:
        assert False


@then('User delete the respective team via "{team_name}"')
def step_impl(context, team_name):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Team_Name_Search_InputField__XPATH)
    context.ele_ops.clear(oR.Team_Name_Search_InputField__XPATH)
    context.ele_ops.send_keys(oR.Team_Name_Search_InputField__XPATH, team_name)
    context.ele_ops.wait_until_elements_present(oR.Teams_list__XPATH)
    context.ele_ops.wait_until_element_present_visible(oR.Delete_team__XPATH)
    context.ele_ops.click(oR.Delete_team__XPATH)
    context.ele_ops.wait_until_element_present_visible(oR.Delete_the_record__XPATH)
    context.ele_ops.click(oR.Delete_the_record__XPATH)


@then('Verify User successfully deleted "{team_name}" from Team')
def step_impl(context, team_name):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Team_Name_Search_InputField__XPATH)
    context.ele_ops.clear(oR.Team_Name_Search_InputField__XPATH)
    context.ele_ops.send_keys(oR.Team_Name_Search_InputField__XPATH, team_name)
    context.ele_ops.wait_until_elements_present(oR.Teams_list__XPATH)
    ele_texts = [ele.text for ele in context.ele_ops.find_elements(oR.Teams_list__XPATH)]
    if len(ele_texts) == 0:
        assert True


@then('User click on view for corresponding "{team_Name}" to view details')
def step_impl(context, team_Name):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Team_Name_Search_InputField__XPATH)
    context.ele_ops.clear(oR.Team_Name_Search_InputField__XPATH)
    context.ele_ops.send_keys(oR.Team_Name_Search_InputField__XPATH, team_Name)
    context.ele_ops.wait_until_elements_present(oR.Teams_list__XPATH)
    context.ele_ops.click(oR.View_team__XPATH)


@then('Verify User able to view "{team_name}"')
def step_impl(context, team_name):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Project_Details_view__XPATH)
    assert context.ele_ops.get_element_text(oR.Team_Name__ID) == team_name


@then("Close the View Pop up")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.Close__XPATH)
    context.ele_ops.click(oR.Close__XPATH)


@then("User enter details in respective fields")
def step_impl(context):
    for row in context.table:
        print(row["email"],row["password"])


@when('User Successfully login into the application with valid credentials')
def step_impl(context):
    context.execute_steps('''
    Given User navigated to seo marketing landing page
    Then User enter "sandeep.agarwal@khamelia.net" and "Pass@123" in respective fields
    Then User clicked on sign In
    Then User must be successfully navigated to the Dashboard
    ''')
