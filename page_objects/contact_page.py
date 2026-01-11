
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    MESSAGE_LABEL = (By.CSS_SELECTOR, ".h4.mb-4.text-center")
    NAME_INPUT = (By.CSS_SELECTOR, "#name")
    NAME = "SLIM SHADY"
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    EMAIL_ADDRESS = "Slimshady30@yopmail.com"
    PHONE_INPUT = (By.CSS_SELECTOR, "#phone")
    PHONE_NUMBER = "25567489011"
    SUBJECT_INPUT = (By.CSS_SELECTOR, "#subject")
    SUBJECT = "Testing"
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, "#description")
    MESSAGE = "The few things I'm sure of"
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")



    @property
    def message_label(self):
        """Get message label element"""
        return self.driver.find_element(By.CSS_SELECTOR, ".h4.mb-4.text-center")


    @property
    def name_input(self):
        """Get name input element"""
        return self.driver.find_element(By.CSS_SELECTOR, "#name")


    @property
    def email_input(self):
        """Get email input element"""
        return self.driver.find_element(By.CSS_SELECTOR, "#email")


    @property
    def phone_input(self):
        """Get phone input element"""
        return self.driver.find_element(By.CSS_SELECTOR, "#phone")

    @property
    def subject_input(self):
        """Get subject input element"""
        return self.driver.find_element(By.CSS_SELECTOR, "#subject")

    @property
    def message_textarea(self):
            """Get message textarea element"""
            return self.driver.find_element(By.CSS_SELECTOR, "#description")

    @property
    def submit_button(self):
        """Get submit button element"""
        return self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")


    def enter_contact_form(self, name=None, email=None, phone=None, subject=None, message=None):
        """Fill complete contact form"""
        if name:
            self.name_input.clear()
            self.name_input.send_keys("SLIM SHADY")
        if email:
            self.email_input.clear()
            self.email_input.send_keys("Slimshady30@yopmail.com")
        if phone:
            self.phone_input.clear()
            self.phone_input.send_keys(25567489011)
        if subject:
            self.subject_input.clear()
            self.subject_input.send_keys("Testing")
        if message:
            self.message_textarea.clear()
            self.message_textarea.send_keys("The few things I'm sure of")

    def submit_contact_form(self):
        """Click submit button"""
        self.submit_button.click()


      #ThankYou confirmation page after successful submission
    @property
    def header(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.card-body h3.h4.mb-4")

    @property
    def first_paragraph(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.card-body p:nth-of-type(1)")

    @property
    def bold_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.card-body p[style='font-weight: bold;']")

    @property
    def second_paragraph(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.card-body p:nth-of-type(3)")

    def get_header_text(self):
        return self.header.text.strip()

    def get_first_paragraph_text(self):
        return self.first_paragraph.text.strip()

    def get_bold_text(self):
        return self.bold_text.text.strip()

    def get_second_paragraph_text(self):
        return self.second_paragraph.text.strip()


      #alertPage for unsuccessful submission
    @property
    def alert_box(self):
        return self.driver.find_element(By.CLASS_NAME, "alert-danger")

    @property
    def alert_messages(self):
        return self.alert_box.find_elements(By.TAG_NAME, "p")

    def get_alert_message_texts(self):
        return [message.text.strip() for message in self.alert_messages]