

from behave import given, then
from page_objects.location_page import LocationPage
import time

@given('I am on the hotel location page')
def step_navigate_to_location_page(context):
    context.driver.get(context.base_url)
    time.sleep(5)
    context.location_page = LocationPage(context.driver)
    context.location_page.scroll_to_location()
    time.sleep(5)

@then('the page header should be "{expected_header}"')
def step_impl(context, expected_header):
    actual_header = context.location_page.get_header_text()
    assert actual_header == expected_header, \
        f"Expected '{expected_header}', got '{actual_header}'"

@then('the location description should be "{expected_description}"')
def step_verify_description(context, expected_description):
    assert context.location_page.location_description.text == expected_description

@then('the address should be "{expected_address}"')
def step_verify_address(context, expected_address):
    assert context.location_page.address.text == expected_address

@then('the phone number should be "{expected_phone}"')
def step_verify_phone(context, expected_phone):
    assert context.location_page.phone.text == expected_phone

@then('the email should be "{expected_email}"')
def step_verify_email(context, expected_email):
    assert context.location_page.email.text == expected_email

@then('the getting here section should contain "{partial_text}"')
def step_verify_getting_here(context, partial_text):
    assert partial_text in context.location_page.getting_here_text.text
