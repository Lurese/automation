# features/environment.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def before_all(context):
    """Setup before all tests - runs once"""
    context.base_url = 'https://automationintesting.online/'
    print(f"\n🌐 Base URL set to: {context.base_url}")


def before_scenario(context, scenario):
    """Setup before each scenario"""
    print(f"\n🚀 Starting scenario: {scenario.name}")

    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)

    print(f"✅ Browser opened successfully")


def after_scenario(context, scenario):
    """Cleanup after each scenario"""
    print(f"\n🏁 Finished scenario: {scenario.name} - Status: {scenario.status}")

    if scenario.status == "failed":
        print("❌ Scenario FAILED - Keeping browser open for 5 seconds")
        time.sleep(5)

    if hasattr(context, 'driver'):
        context.driver.quit()
        print("🔒 Browser closed")


def after_all(context):
    """Cleanup after all tests"""
    pass




# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
#
# # from page_objects.availability_page import AvailabilityPage
#
#
# def before_scenario(context, scenario):
#     """Setup before each scenario"""
#     chrome_options = Options()
#     chrome_options.add_argument('--start-maximized')
#     chrome_options.add_argument('--disable-notifications')
#     # Keep browser open longer to see what's happening
#     chrome_options.add_experimental_option("detach", True)  # This keeps browser open!
#
#     context.driver = webdriver.Chrome(options=chrome_options)
#     context.driver.implicitly_wait(10)
#     context.base_url = 'https://automationintesting.online/'
#
#
# def after_scenario(context, scenario):
#     """Cleanup after each scenario"""
#     print(f"\n🏁 Finished scenario: {scenario.name} - Status: {scenario.status}")
#     if hasattr(context, "driver") and context.driver:
#        context.driver.quit()
#
#     if scenario.status == "failed":
#         print("❌ Scenario FAILED - Browser will stay open for debugging")
#         time.sleep(5)  # Wait 5 seconds before closing on failure



#         OR YOU CAN DO YOUR ENVIRONMENT SETUP LIKE THIS
#           UNCOMMENT TO FIND OUT BUT THE ENVIRONMENT ON TOP HAS TO BE COMMENTED OUT
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# def before_all(context):
#     chrome_options = Options()
#     chrome_options.add_argument('--start-maximized')
#
#     context.driver = webdriver.Chrome(options=chrome_options)
#     context.driver.implicitly_wait(10)
#
# def before_scenario(context, scenario):
#     context.driver.get("https://automationintesting.online/")
#
# def after_all(context):
#     context.driver.quit()
