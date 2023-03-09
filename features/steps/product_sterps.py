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
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.get_url(str(test_site_url))


@when("Verify User successfully landed on home page")
def step_impl(context):
    print(context.ele_ops.get_window_title())


@then("User moved to and clicked resources option")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    resource_sign = context.ele_ops.get_locator_signature("resources__XPATH")
    resource = config.get("LOCATORS", "resources__XPATH")
    context.ele_ops.wait_until_element_present_visible("resources__XPATH")
    # context.ele_ops.move_to_element(resource_sign, resource).perform_after_actionChains()
    # resource_practice_site = config.get("LOCATORS", "resource_practice_site")
    # resource_sign = context.ele_ops.get_locator_signature("resources__XPATH")
    # context.ele_ops.click(resource_sign, resource_practice_site)


@then("Verify User landed on Dummy Registration Page")
def step_impl(context):
    print(context.ele_ops.get_window_title())


@then('User fill "{name}" in Dummy Registration form')
def step_impl(context, name):
    # context.ele_ops.wait_until_element_present_visible("name__XPATH")
    # context.ele_ops.find_element("name__XPATH")
    # context.ele_ops.send_keys("name__XPATH", name)
    time.sleep(1)
