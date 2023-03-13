import configparser
import os

from behave import *
from behave import use_step_matcher
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import oR
from Selenium_Operations.Element_Operations import Element_Operations

use_step_matcher('parse')

conf_path = "../../conf.ini"

this_folder = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(this_folder, '../../conf.ini')
config = configparser.RawConfigParser()
res = config.read(init_file)
browsers = config.get('BASIC_CONFIGS', 'browser').split(",")
headless = config.get('BASIC_CONFIGS', 'headless')
implicit_wait = config.get('BASIC_CONFIGS', 'implicit_wait')
test_site_url = config.get('BASIC_CONFIGS', 'test_site_url')


@given("User navigated to Landing page")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.get_url(test_site_url)


@when("Verify User successfully landed on home page")
def step_impl(context):
    print(context.ele_ops.get_window_title())


@then("User moved to and clicked resources option")
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.wait_until_element_present_visible(oR.resources__XPATH)
    context.ele_ops.move_to_element(oR.resources__XPATH).perform_after_actionChains()
    context.ele_ops.click(oR.resources_practice_site_1__XPATH)


@then("Verify User landed on Dummy Registration Page")
def step_impl(context):
    print(context.ele_ops.get_window_title())


@then('User fill "{name}" "{phone}" "{email}" "{country}" "{city}" "{username}" {password} in Dummy Registration form')
def step_impl(context, name, phone, email, country, city, username, password):
    context.ele_ops = Element_Operations(context.driver)

    context.ele_ops.wait_until_element_present_visible(oR.name__XPATH)
    context.ele_ops.send_keys(oR.name__XPATH, name)

    context.ele_ops.wait_until_element_present_visible(oR.phone__CSS)
    context.ele_ops.send_keys(oR.phone__CSS, phone)

    context.ele_ops.wait_until_element_present_visible(oR.email__NAME)
    context.ele_ops.send_keys(oR.email__NAME, email)

    context.ele_ops.wait_until_element_present_visible(oR.country__XPATH)
    context.ele_ops.select_by_value(oR.country__XPATH, country)

    context.ele_ops.wait_until_element_present_visible(oR.city__XPATH)
    context.ele_ops.send_keys(oR.city__XPATH, city)

    context.ele_ops.wait_until_element_present_visible(oR.username__XPATH)
    context.ele_ops.send_keys(oR.username__XPATH, username)

    context.ele_ops.wait_until_element_present_visible(oR.password__XPATH)
    context.ele_ops.send_keys(oR.password__XPATH, password)
