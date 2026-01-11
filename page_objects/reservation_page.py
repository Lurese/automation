
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class RoomBookingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    #Locator
    ROOM_TITLE = (By.CSS_SELECTOR, "h1.fw-bold.mb-2")
    ROOM_IMAGE = (By.CSS_SELECTOR, "img[alt='Room Image']")
    ROOM_DESCRIPTION = (By.CSS_SELECTOR, "h2.fs-4.fw-bold.mb-3 + p")
    ROOM_FEATURES = (By.CSS_SELECTOR, ".amenity-icon")
    ROOM_POLICIES = (By.CSS_SELECTOR, ".fs-5.mb-3")
    CALENDAR_BUTTON = (By.CSS_SELECTOR, ".rbc-button-link")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".fw-bold span:last-child")
    RESERVE_BUTTON = (By.ID, "doReservation")

    @property
    def room_title(self):
        return self.driver.find_element(*self.ROOM_TITLE).text

    @property
    def room_image(self):
        return self.driver.find_element(*self.ROOM_IMAGE).get_attribute("src")

    @property
    def room_description(self):
        return self.driver.find_element(*self.ROOM_DESCRIPTION).text
    def get_room_description_text(self):
        return self.room_description.text.strip()

    @property
    def room_features(self):
        return self.driver.find_elements(*self.ROOM_FEATURES)
    def get_room_features_text(self):
        return [feature.text.strip() for feature in self.room_features]

    @property
    def room_policies(self):
        return self.driver.find_element(*self.ROOM_POLICIES)
    def get_room_policies_text(self):
        return [policy.text.strip() for policy in self.room_policies]


    @property
    def calendar_buttons(self):
        return self.driver.find_elements(*self.CALENDAR_BUTTON)
    def select_date(self, date):
        for button in self.calendar_buttons:
            if button.text == str(date):
                button.click()
                break

    @property
    def total_price(self):
        return self.driver.find_element(*self.TOTAL_PRICE).text

    @property
    def reserve_button(self):
        return self.driver.find_element(*self.RESERVE_BUTTON)

    def click_reserve(self):
        self.reserve_button.click()

    # Locators
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, ".room-firstname")
    firstname = "Slim"
    LASTNAME_INPUT = (By.CSS_SELECTOR, ".room-lastname")
    lastname = "Shady"
    EMAIL_INPUT = (By.CSS_SELECTOR, ".room-email")
    email = "Slimshady30@yopmail.com"
    PHONE_INPUT = (By.CSS_SELECTOR, ".room-phone")
    phone = 25567489011
    RESERVE_NOW_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.w-100.mb-3")
    CANCEL_BUTTON = (By.CSS_SELECTOR, ".btn.btn-secondary.w-100.mb-3")


    @property
    def firstname_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".room-firstname")
    def enter_firstname(self, firstname):
        return self.firstname_input.send_keys(firstname)


    @property
    def lastname_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".room-lastname")
    def enter_lastname(self, lastname):
        return self.lastname_input.send_keys(lastname)


    @property
    def email_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".room-email")
    def enter_email(self, email):
        return self.email_input.send_keys(email)


    @property
    def phone_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".room-phone")
    def enter_phone(self, phone):
        return self.phone_input.send_keys(phone)


    @property
    def reserve_now_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.w-100.mb-3")

    def click_reserve_now_button(self):
        self.reserve_now_button.click()
        time.sleep(5)


    @property
    def cancel_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-secondary.w-100.mb-3")
    def click_cancel(self):
        self.cancel_button.click()




















