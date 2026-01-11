
from behave import given, when, then
from page_objects.homepage_page import HomePage
import time

@given("I am on the home page")
def step_impl(context):
    context.driver.get(context.base_url)
    context.home = HomePage(context.driver)
    time.sleep(2)

@then('the title should be "Welcome to Shady Meadows B&B"')
def step_impl(context):
    expected = "Welcome to Shady Meadows B&B"
    actual = context.home.get_title_text()
    assert actual == expected, \
            f"Expected '{expected}', but got '{actual}'"
    time.sleep(2)

@then("the description should be correct")
def step_impl(context):
    desc = context.home.get_description_text()
    assert "Welcome to Shady Meadows" in desc
    assert "A place so beautiful" in desc
    assert "comfortable beds" in desc
    time.sleep(2)

