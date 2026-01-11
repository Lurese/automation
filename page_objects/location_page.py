

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time



class LocationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    LOCATION = (By.XPATH, "//h2[normalize-space()='Our Location']")
    LOCATION_DESCRIPTION = (By.XPATH, "//section[@id='location']//p[@class='lead text-muted']")
    ADDRESS = (By.XPATH, "//h5[text()='Address']/following-sibling::p")
    PHONE = (By.XPATH, "//h5[text()='Phone']/following-sibling::p")
    EMAIL = (By.XPATH, "//h5[text()='Email']/following-sibling::p")
    GETTING_HERE_TEXT = (By.XPATH, "//h4[text()='Getting Here']/following-sibling::p")

    @property
    def location (self):
        """Get header element"""
        return self.driver.find_element(By.XPATH, "//h2[normalize-space()='Our Location']")
    def scroll_to_location(self):
        try:
            element = self.location
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)
        except Exception as e:
            print(f"Error scrolling: {e}")
    def get_header_text(self):
        """Get header text"""
        return self.location.text

    @property
    def location_description(self):
        """Get location description element"""
        return self.driver.find_element(By.XPATH, "//section[@id='location']//p[@class='lead text-muted']")
    def get_location_description_text(self):
        """Get location description text"""
        return self.location_description.text

    @property
    def address(self):
        """Get address element"""
        return self.driver.find_element(By.XPATH, "//h5[text()='Address']/following-sibling::p")
    def get_address_text(self):
        """Get address text"""
        return self.address.text

    @property
    def phone(self):
        """Get phone element"""
        return self.driver.find_element(By.XPATH, "//h5[text()='Phone']/following-sibling::p")
    def get_phone_text(self):
        """Get phone text"""
        return self.phone.text

    @property
    def email(self):
        """Get email element"""
        return self.driver.find_element(By.XPATH, "//h5[text()='Email']/following-sibling::p")
    def get_email_text(self):
        """Get email text"""
        return self.email.text

    @property
    def getting_here_text(self):
        """Get getting here text element"""
        return self.driver.find_element(By.XPATH, "//h4[text()='Getting Here']/following-sibling::p")
    def get_getting_here_text(self):
        """Get getting here text"""
        return self.getting_here_text.text




