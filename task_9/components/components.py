from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WebElement:
    def __init__(self, driver, locator=''):
        self.locator = locator
        self.driver = driver

    def click(self):
        """ Click the element. """
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def visible(self):
        return self.find_element().is_displayed()

    def not_visible(self, time_wait=2):
        try:
            WebDriverWait(self.driver, time_wait).until_not(EC.invisibility_of_element((By.CSS_SELECTOR, self.locator)))
            return False
        except TimeoutException:
            return True

    def get_text(self):
        """ Get text of the element. """
        return str(self.find_element().text)