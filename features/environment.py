import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
# def before_all(context):
#     print("Executes before everything.")


# def before_feature(context, feature):
#     print(" Executes before every feature.")

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)


# def before_step(context, step):
#     print("   Executes before every step.")


# def before_tag(context, tag):
#     print("    Executes before every tag.")


# def after_all(context):
#     print("Executes after everything.")


# def after_feature(context, feature):
#     print(" Executes after every feature.")


def after_scenario(context, driver):
    time.sleep(1)
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)


# def after_tag(context, tag):
#     print("    Executes after every tag.")
