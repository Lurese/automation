# steps/rooms_steps.py
from behave import given, when, then
from page_objects.rooms_page import RoomsPage
from selenium.webdriver.common.by import By
import time


@given("I navigate to the Rooms page")
def step_navigate_to_rooms(context):
    """Navigate to rooms page and scroll to Our Rooms section"""
    print(f"\n📍 Navigating to: {context.base_url}")
    context.driver.get(context.base_url)
    time.sleep(3)

    context.rooms_page = RoomsPage(context.driver)
    context.rooms_page.scroll_to_our_rooms_section()
    time.sleep(2)
    print("✅ On Rooms page")


@then('the rooms page title should be "{expected_title}"')
def step_verify_rooms_title(context, expected_title):
    """Verify 'Our Rooms' title"""
    actual_title = context.rooms_page.rooms_title.text
    assert actual_title == expected_title, \
        f"Expected '{expected_title}', got '{actual_title}'"
    print(f"✅ Title verified: {actual_title}")


@then('the rooms subtitle should be "{expected_subtitle}"')
def step_verify_rooms_subtitle(context, expected_subtitle):
    """Verify rooms subtitle"""
    actual_subtitle = context.rooms_page.rooms_subtitle.text
    assert actual_subtitle == expected_subtitle, \
        f"Expected '{expected_subtitle}', got '{actual_subtitle}'"
    print(f"✅ Subtitle verified")


@then("all three room images should be displayed")
def step_verify_room_images(context):
    """Verify all 3 room images are displayed and visible"""

    # Method 1: Get image sources
    images = context.rooms_page.get_all_room_images()
    print(f"\n📦 Found {len(images)} room image sources")

    assert len(images) == 3, f"Expected 3 images, found {len(images)}"

    # Verify image sources are valid
    for i, img_src in enumerate(images):
        assert img_src is not None, f"Image {i + 1} not found"
        assert img_src != "", f"Image {i + 1} has no source"
        print(f"  ✅ Room {i + 1} image source: {img_src[:60]}...")

    # Method 2: Also verify images are displayed on page
    cards = context.rooms_page.room_cards
    visible_count = 0

    for i, card in enumerate(cards):
        try:
            img_element = card.find_element(By.TAG_NAME, "img")
            if img_element.is_displayed():
                visible_count += 1
                print(f"  ✅ Room {i + 1} image is visible on page")
            else:
                print(f"  ⚠️ Room {i + 1} image exists but not visible")
        except Exception as e:
            print(f"  ❌ Room {i + 1} image check failed: {e}")

    assert visible_count == 3, f"Expected 3 visible images, found {visible_count}"
    print("✅ All 3 room images verified and displayed")


@then("the room titles should be:")
def step_verify_room_titles(context):
    """Verify room titles from table"""
    expected_titles = [row[0] for row in context.table]
    actual_titles = context.rooms_page.get_all_room_titles()

    print(f"Expected: {expected_titles}")
    print(f"Actual: {actual_titles}")

    for expected in expected_titles:
        assert expected in actual_titles, \
            f"'{expected}' not found in {actual_titles}"

    print("✅ All room titles verified")


@then("all rooms should have descriptions displayed")
def step_verify_room_descriptions(context):
    """Verify all rooms have description text"""
    descriptions = context.rooms_page.get_all_room_descriptions()

    assert len(descriptions) == 3, f"Expected 3 descriptions, found {len(descriptions)}"

    for i, desc in enumerate(descriptions):
        assert desc is not None, f"Room {i + 1} has no description"
        assert len(desc) > 10, f"Room {i + 1} description too short: {desc}"
        print(f"  ✅ Room {i + 1} description: {desc[:50]}...")

    print("✅ All room descriptions verified")


@then("all rooms should have features displayed")
def step_verify_room_features(context):
    """Verify all rooms have features (WiFi, TV, etc.)"""
    all_features = context.rooms_page.get_all_room_features()

    assert len(all_features) == 3, f"Expected features for 3 rooms"

    for i, features in enumerate(all_features):
        print(f"  Room {i + 1} features: {features}")
        assert len(features) > 0, f"Room {i + 1} has no features"

    print("✅ All room features verified")


@then("the room prices should be:")
def step_verify_room_prices(context):
    """Verify room prices from table"""
    expected_prices = [row[0] for row in context.table]
    actual_prices = context.rooms_page.get_all_room_prices()

    print(f"Expected prices: {expected_prices}")
    print(f"Actual prices: {actual_prices}")

    for expected in expected_prices:
        assert expected in actual_prices, \
            f"Price '{expected}' not found in {actual_prices}"

    print("✅ All room prices verified")


@when('I click Book Now for the "{room_type}" room')
def step_click_book_now(context, room_type):
    """Click Book Now for specific room"""
    room_map = {
        "Single": 0,
        "Double": 1,
        "Suite": 2
    }

    index = room_map.get(room_type)
    assert index is not None, f"Unknown room type: {room_type}"

    context.rooms_page.click_book_now_by_index(index)
    context.expected_room_id = str(index + 1)  # Room IDs are 1, 2, 3
    print(f"✅ Clicked Book Now for {room_type}")


@then("I should be redirected to the reservation page")
def step_verify_on_reservation_page(context):
    """Verify on reservation page"""
    assert context.rooms_page.is_on_reservation_page(), \
        f"Not on reservation page. Current URL: {context.driver.current_url}"
    print("✅ On reservation page")


@then('I should be on the reservation page for room "{room_id}"')
def step_verify_reservation_room_id(context, room_id):
    """Verify on reservation page for specific room"""
    actual_room_id = context.rooms_page.get_current_reservation_room_id()
    assert actual_room_id == room_id, \
        f"Expected room {room_id}, but on room {actual_room_id}"
    print(f"✅ On reservation page for room {room_id}")









# # steps/rooms_steps.py
# from behave import given, when, then
# from page_objects.rooms_page import RoomsPage
# import time
#
#
# @given("I navigate to the Rooms page")
# def step_impl(context):
#     """Navigate to the rooms page and scroll to Our Rooms section"""
#     print(f"\n📍 Navigating to: {context.base_url}")
#
#     try:
#         context.driver.get(context.base_url)
#         print(f"✅ Page loaded: {context.driver.title}")
#
#         time.sleep(5)  # Wait 5 seconds for page to fully load
#
#         print("📄 Initializing RoomsPage...")
#         context.rooms = RoomsPage(context.driver)
#
#         print("⬇️ Scrolling to Our Rooms section...")
#         context.rooms.scroll_to_our_rooms_section()
#
#         time.sleep(3)  # Wait for scroll
#         print("✅ Ready for test assertions")
#
#     except Exception as e:
#         print(f"❌ Error in Given step: {e}")
#         raise
#
#
# @then('the rooms page title should be "{expected_title}"')
# def step_impl(context, expected_title):
#     """Verify the rooms page title"""
#     try:
#         actual_title = context.rooms.title.text
#         print(f"📝 Expected: '{expected_title}' | Actual: '{actual_title}'")
#         assert actual_title == expected_title, \
#             f"Expected title '{expected_title}', but got '{actual_title}'"
#         print("✅ Title verification PASSED")
#     except Exception as e:
#         print(f"❌ Title verification FAILED: {e}")
#         raise
#
#
# @then('the rooms subtitle should be "{expected_subtitle}"')
# def step_impl(context, expected_subtitle):
#     """Verify the rooms subtitle"""
#     try:
#         actual_subtitle = context.rooms.subtitle.text
#         print(f"📝 Expected subtitle: '{expected_subtitle}'")
#         print(f"📝 Actual subtitle: '{actual_subtitle}'")
#         assert actual_subtitle == expected_subtitle, \
#             f"Expected subtitle '{expected_subtitle}', but got '{actual_subtitle}'"
#         print("✅ Subtitle verification PASSED")
#     except Exception as e:
#         print(f"❌ Subtitle verification FAILED: {e}")
#         raise
#
#
# @then("the room titles should be:")
# def step_impl(context):
#     """Verify room titles from table"""
#     try:
#         expected_titles = [row[0] for row in context.table]
#         actual_titles = context.rooms.get_all_room_titles()
#
#         print(f"📝 Expected titles: {expected_titles}")
#         print(f"📝 Actual titles: {actual_titles}")
#
#         for expected_title in expected_titles:
#             assert expected_title in actual_titles, \
#                 f"Expected room title '{expected_title}' not found. Available: {actual_titles}"
#         print("✅ Room titles verification PASSED")
#     except Exception as e:
#         print(f"❌ Room titles verification FAILED: {e}")
#         raise
#
#
# @then("the room prices should be:")
# def step_impl(context):
#     """Verify room prices from table"""
#     try:
#         expected_prices = [row[0] for row in context.table]
#         actual_prices = context.rooms.get_all_room_prices()
#
#         print(f"📝 Expected prices: {expected_prices}")
#         print(f"📝 Actual prices: {actual_prices}")
#
#         for expected_price in expected_prices:
#             assert expected_price in actual_prices, \
#                 f"Expected price '{expected_price}' not found. Available: {actual_prices}"
#         print("✅ Room prices verification PASSED")
#     except Exception as e:
#         print(f"❌ Room prices verification FAILED: {e}")
#         raise




# from behave import given, when, then
# from page_objects.rooms_page import RoomsPage
# import time
#
#
# @given("I navigate to the Rooms page")
# def step_impl(context):
#     context.driver.get(context.base_url)
#     time.sleep(5)
#     # context.home.rooms_link.click()
#     context.rooms = RoomsPage(context.driver)
#     context.rooms.scroll_to_our_rooms_section()
#     time.sleep(5)
#
# @then('the rooms page title should be "{expected_title}"')
# def step_impl(context, expected_title):
#     assert context.rooms.title.text == expected_title
#
# @then('the rooms subtitle should be "{expected_subtitle}"')
# def step_impl(context, expected_subtitle):
#     assert context.rooms.subtitle.text == expected_subtitle
#
# @then("the room titles should be:")
# def step_impl(context):
#     expected_titles = [row[0] for row in context.table]
#     for index, expected in enumerate(expected_titles):
#         assert context.rooms.get_room_title(index) == expected
#
# @then("the room prices should be:")
# def step_impl(context):
#     expected_prices = [row[0] for row in context.table]
#     for index, expected in enumerate(expected_prices):
#         assert context.rooms.get_room_price(index) == expected
#
# @when("I book room at index {index}")
# def step_impl(context, index):
#     index = int(index)
#     context.rooms.book_room(index)
#
# @then('I should be redirected to "{path}"')
# def step_impl(context, path):
#     assert path in context.driver.current_url
