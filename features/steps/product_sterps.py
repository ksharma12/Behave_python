import configparser
import os
import time

from behave import *
from behave import use_step_matcher
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from features.steps.Selenium_Operations.Element_Operations import Element_Operations
from features.steps.Utils.Common_Operations import Common_Operations

use_step_matcher('parse')

conf_path = "conf.ini"

this_folder = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(this_folder, 'conf.ini')
config = configparser.RawConfigParser()
res = config.read(init_file)
browsers = config.get('BASIC_CONFIGS', 'browser').split(",")
headless = config.get('BASIC_CONFIGS', 'headless')
implicit_wait = config.get('BASIC_CONFIGS', 'implicit_wait')
test_site_url = config.get('BASIC_CONFIGS', 'test_site_url')


@given("I navigate to google.com")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("https://www.google.com/")
    print("I navigate to google.com")


@when("I Validate the Page title")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    title = context.driver.title
    assert title == "Google"
    print(title)
    print("I Validate the Page title")


@step("I click the search button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    print("And I click the search button")


@then('I enter the text as "{search_text}"')
def step_impl(context, search_text):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.NAME, "q").send_keys(search_text)
    print(f"The entered text is {search_text}")


@given("User navigated to Landing page")
def step_impl(context):
    context.ele_ops = Element_Operations(conf_path, "LOCATOR", context.driver)
    context.ele_ops.get_url(str(test_site_url))


@when("Verify User successfully landed on home page")
def step_impl(context):
    print(context.ele_ops.get_window_title())


@then("User moved to and clicked resources option")
def step_impl(context):
    context.ele_ops = Element_Operations(conf_path, "LOCATORS", context.driver)
    context.ele_ops.wait_until_element_present_visible("resources__XPATH")
    # context.ele_ops.move_to_element("resources__XPATH").perform_after_actionChains()
    # context.ele_ops.click("resources_practice_site_1__XPATH")


@then("Verify User landed on Dummy Registration Page")
def step_impl(context):
    print(context.ele_ops.get_window_title())


@then('User fill "{name}" "{phone}" "{email}" "{country}" "{city}" "{username}" {password} in Dummy Registration form')
def step_impl(context, name, phone, email, country, city, username, password):
    pass
    # context.ele_ops = Element_Operations("./steps/conf.ini", "LOCATORS", context.driver)
    #
    # context.ele_ops.wait_until_element_present_visible("name__XPATH")
    # context.ele_ops.send_keys("name__XPATH", name)
    #
    # context.ele_ops.wait_until_element_present_visible("phone__CSS")
    # context.ele_ops.send_keys("phone__CSS", phone)
    #
    # context.ele_ops.wait_until_element_present_visible("email__NAME")
    # context.ele_ops.send_keys("email__NAME", email)
    #
    # context.ele_ops.wait_until_element_present_visible("country__XPATH")
    # context.ele_ops.select_by_value("country__XPATH", country)
    #
    # context.ele_ops.wait_until_element_present_visible("city__XPATH")
    # context.ele_ops.send_keys("city__XPATH", city)
    #
    # context.ele_ops.wait_until_element_present_visible("username__XPATH")
    # context.ele_ops.send_keys("username__XPATH", username)
    #
    # context.ele_ops.wait_until_element_present_visible("password__XPATH")
    # context.ele_ops.send_keys("password__XPATH", password)
