
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.contact_page import ContactPage


@given("I am on the hotel contact page")
def step_open_contact_page(context):
    context.driver.get(context.base_url)
    context.contact = ContactPage(context.driver)


@when("I enter valid contact details")
def step_enter_valid_details(context):
    context.contact.enter_contact_form(
        name=True,
        email=True,
        phone=True,
        subject=True,
        message=True
    )


@when("I submit the contact form")
def step_submit_form(context):
    context.contact.submit_contact_form()

    # Wait for Thank You page to display
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.card-body h3.h4.mb-4"))
    )


@then("the thank you message should be displayed correctly")
def step_verify_thank_you_page(context):
    assert context.contact.get_header_text() == "Thanks for getting in touch SLIM SHADY!"
    assert "We'll get back to you about" in context.contact.get_first_paragraph_text()
    assert context.contact.get_bold_text() == "Testing"
    assert "as soon as possible." in context.contact.get_second_paragraph_text()


@when("I submit the contact form without entering any details")
def step_submit_empty_form(context):
    context.contact.submit_contact_form()

    # Wait for alert messages
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
    )


@then("all alert error messages should be displayed")
def step_verify_alert_messages(context):
    alerts = context.contact.get_alert_message_texts()

    # Expected number of alert messages
    expected_count = 8
    assert len(alerts) == expected_count, f"Expected {expected_count}, got {len(alerts)}"

    # Validate specific messages
    assert "Name may not be blank" in alerts
    assert "Email may not be blank" in alerts
    assert "Phone must be between 11 and 21 characters." in alerts
    assert "Phone may not be blank" in alerts
    assert "Subject must be between 5 and 100 characters" in alerts
    assert "Subject may not be blank" in alerts
    assert "Message must be between 20 and 2000 characters" in alerts
    assert "Message may not be blank" in alerts
