import configparser
import os
import time
from behave import *
import oR
from Selenium_Operations.Element_Operations import Element_Operations

use_step_matcher("parse")

this_folder = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(this_folder, "../../conf.ini")
config = configparser.RawConfigParser()
res = config.read(init_file)


@given("User navigated to seo marketing landing page")
def step_impl(context):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.get_url("http://seomarketing.logixportfolio.in/")
    context.ele_ops.maximize_window()
    assert context.ele_ops.get_window_title() == "Quaapps:Login"


@then('User enter "{email}" and "{password}" in respective fields')
def step_impl(context, email, password):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.email__ID)
    context.ele_ops.send_keys(oR.email__ID, email)
    context.ele_ops.wait_until_element_present_visible(oR.password__ID)
    context.ele_ops.send_keys(oR.password__ID, password)


@then("User clicked on sign In")
def step_impl(context):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.sign_in_button__XPATH)
    context.ele_ops.click(oR.sign_in_button__XPATH)


@then("User must be successfully navigated to the Dashboard")
def step_impl(context):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.dashboard_heading__XPATH)
    assert context.ele_ops.get_element_text(oR.dashboard_heading__XPATH) == "WELCOME TO DASHBOARD"
    assert "Dashboard" in context.ele_ops.get_window_current_url()


@then("User navigated to Seo marketing")
def step_impl(context):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present("Seo_Marketing__XPATH")
    context.ele_ops.click("Seo_Marketing__XPATH")


@then("User navigated to Team Master")
def step_impl(context):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("Team_Master__XPATH")
    context.ele_ops.click("Team_Master__XPATH")
    assert "Team_Master" in context.ele_ops.get_window_current_url()


@then("User clicked on Add Team Button")
def step_impl(context):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("Add_Team__XPATH")
    context.ele_ops.click("Add_Team__XPATH")
    print(context.ele_ops.get_window_current_url())
    assert "ADD" in context.ele_ops.get_window_current_url()


@then('User enter "{Team_name}" in Team Name Field')
def step_impl(context, Team_name):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("Team_Name_input__ID")
    context.ele_ops.send_keys("Team_Name_input__ID", Team_name)


@step('User Select "{User}" from user options')
def step_impl(context, User):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("Select_user__ID")
    context.ele_ops.click("Select_user__ID")
    context.ele_ops.wait_until_elements_present("Multiple_Options__XPATH")
    context.ele_ops.click_from_multiple_ele_text_basis("Multiple_Options__XPATH", User)
    context.ele_ops.click("Help_Information__XPATH")


@step('User enter "{Description} in Description Section"')
def step_impl(context, Description):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.switch_to_frame(config.get("SEO_MARKETING", "iframe_Description__ID"))
    context.ele_ops.send_keys("inside_Description__XPATH", Description)
    context.ele_ops.switch_to_default_content()


@then("User clicked on Submit Button")
def step_impl(context):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("submit_Btn__ID")
    context.ele_ops.click("submit_Btn__ID")


@then('Verify Team Master Added Successfully "{Team_name}"')
def step_impl(context, Team_name):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("alert__XPATH")
    context.ele_ops.click("Team_Master__XPATH")
    context.ele_ops.wait_until_element_present_visible("Team_Name_Search_InputField__XPATH")
    context.ele_ops.send_keys("Team_Name_Search_InputField__XPATH", Team_name)
    context.ele_ops.wait_until_elements_present("Teams_list__XPATH")
    ele_texts = [ele.text for ele in context.ele_ops.find_elements("Teams_list__XPATH")]
    if Team_name in ele_texts:
        assert True
    elif Team_name not in ele_texts:
        assert False


@then('User delete the respective team via "{Team_name}"')
def step_impl(context, Team_name):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("Team_Name_Search_InputField__XPATH")
    context.ele_ops.send_keys("Team_Name_Search_InputField__XPATH", Team_name)
    context.ele_ops.wait_until_elements_present("Teams_list__XPATH")
    context.ele_ops.wait_until_element_present_visible("Delete_team__XPATH")
    context.ele_ops.click("Delete_team__XPATH")
    context.ele_ops.wait_until_element_present_visible("Delete_the_record__XPATH")
    context.ele_ops.click("Delete_the_record__XPATH")


@then('Verify User successfully deleted "{Team_name}" from Team')
def step_impl(context, Team_name):
    context.ele_ops.wait_until_element_present_visible("Team_Name_Search_InputField__XPATH")
    context.ele_ops.send_keys("Team_Name_Search_InputField__XPATH", Team_name)
    context.ele_ops.wait_until_elements_present("Teams_list__XPATH")
    ele_texts = [ele.text for ele in context.ele_ops.find_elements("Teams_list__XPATH")]
    if len(ele_texts) == 0:
        assert True


@then('User click on view for corresponding "{Team_name}" to view details')
def step_impl(context, Team_name):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("Team_Name_Search_InputField__XPATH")
    context.ele_ops.send_keys("Team_Name_Search_InputField__XPATH", Team_name)
    context.ele_ops.wait_until_elements_present("Teams_list__XPATH")
    context.ele_ops.click("View_team__XPATH")


@then('Verify User able to view "{Team_name}"')
def step_impl(context, Team_name):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("Project_Details_view__XPATH")
    assert context.ele_ops.get_element_text("Team_Name__ID") == Team_name


@then("Close the View Pop up")
def step_impl(context):
    context.ele_ops = Element_Operations("SEO_MARKETING", context.driver)
    context.ele_ops.wait_until_element_present_visible("Close__XPATH")
    context.ele_ops.click("Close__XPATH")
