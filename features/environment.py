import time
import allure
from allure_commons.types import AttachmentType
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from Selenium_Operations.Driver_Operations import Driver_Operations


@fixture
def chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.driver = webdriver.Chrome()
    context.driver_ops = Driver_Operations(context.driver)
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver_ops.quit_browser()


@fixture
def chrome_headless(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.options = Options()
    context.options.add_argument('--headless')
    context.options.add_argument('--disable-gpu')
    context.options.add_argument("start-maximized")
    context.options.add_argument("disable-infobars")
    context.options.add_argument("--disable-extensions")
    context.options.add_argument("window-size=1920x1080")
    context.driver = webdriver.Chrome('chromedriver', options=context.options)
    context.driver_ops = Driver_Operations(context.driver)
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver_ops.quit_browser()


@fixture
def firefox(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.driver = webdriver.Firefox()
    context.driver_ops = Driver_Operations(context.driver)
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver_ops.quit_browser()


@fixture
def firefox_headless(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.options = FirefoxOptions()
    context.options.add_argument('--headless')
    context.driver = webdriver.Firefox(options=context.options)
    context.driver_ops = Driver_Operations(context.driver)
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver_ops.quit_browser()


# def before_all(context):
#     print("Executes before everything.")


# def before_feature(context, feature):
#     print(" Executes before every feature.")

def before_scenario(context, scenario):
    for tag in scenario.tags:
        if tag == 'firefox':
            use_fixture(firefox, context)
        elif tag == 'firefox_headless':
            use_fixture(firefox_headless, context)
        elif tag == 'chrome_headless':
            use_fixture(chrome_headless, context)
        elif tag == 'chrome':
            use_fixture(chrome, context)
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
    context
    # time.sleep(1)
    # context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)

# def after_tag(context, tag):
#     print("    Executes after every tag.")
