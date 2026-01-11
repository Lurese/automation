
from behave import given, when, then
from page_objects.availability_page import AvailabilityPage
from datetime import datetime, timedelta
import time


@given("the user is on the check availability page")
def step_impl(context):
    context.driver.get(context.base_url)
    time.sleep(5)
    context.availability = AvailabilityPage(context.driver)
    context.availability.scroll_to_availability_section()
    time.sleep(5)

@then("the default dates should be today and tomorrow")
def step_impl(context):
    default_in = context.availability.get_default_check_in()
    default_out = context.availability.get_default_check_out()

    today = datetime.today().strftime("%d-%m-%Y")
    tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d-%m-%Y")

    assert default_in == today, f"Expected check-in date to be {today}, but got {default_in}"
    assert default_out == tomorrow, f"Expected check-out date to be {tomorrow}, but got {default_out}"


@when('the user enters check-in date "{date}"')
def step_enter_check_in(context, date):
    context.availability.set_check_in(date)


@when('the user enters check-out date "{date}"')
def step_enter_check_out(context, date):
    context.availability.set_check_out(date)


@when("the user clicks check availability")
def step_click_button(context):
    context.availability.click_check_availability()


@then("errors should appear")
def step_errors(context):
    errors = context.availability.error_messages
    assert len(errors) > 0, "Expected errors but none were shown"


@then("no errors should appear")
def step_no_errors(context):
    errors = context.availability.error_messages
    assert len(errors) == 0, f"Expected no errors but found {len(errors)}"


