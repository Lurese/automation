
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h1.display-4")
    def get_title_text(self):
        return self.title.text

    @property
    def description(self):
        return self.driver.find_element(By.CSS_SELECTOR, "p.lead")
    def get_description_text(self):
        return self.description.text



