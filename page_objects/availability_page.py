
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

class AvailabilityPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def availability_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".card-title.text-center.mb-4")
    def scroll_to_availability_section(self):
        """Scroll to the check availability section"""
        try:
            element = self.availability_page
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)  # Wait for scroll to complete
        except Exception as e:
            print(f"Error scrolling: {e}")
    # def scroll_to_availability_section(self):
    #         element = self.availability_page
    #         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @property
    def check_in_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[value='21/11/2025']")
    def set_check_in_date(self, date):
        self.check_in_input.clear()
        self.check_in_input.send_keys(date)
    def get_default_check_in(self):
        return self.check_in_input.get_attribute("value")

    @property
    def check_out_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[value='22/11/2025']")
    def set_check_out_date(self, date):
        self.check_out_input.clear()
        self.check_out_input.send_keys(date)
    def get_default_check_out_date(self):
        self.check_out_input.get_attribute("value")

    @property
    def check_availability_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    def click_check_availability(self):
        return self.check_availability_button.click()

    @property
    def error_messages(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "p.text-danger")








