from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from Locators.all_locators import LocatoresBlaze


class BasePages(LocatoresBlaze):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def setup_demoblaze(self):
        self.driver.get(self.HOME_PAGE)
        self.driver.maximize_window()
        return self.driver

    def find(self, path, locator) -> webelement:
        return self.driver.find_element(path, locator)

    def click(self, path, locator):
        self.wait_until_element_is_visible(path, locator)
        self.find(path, locator).click()

    def fields(self, path, locate, values):
        self.wait_until_element_is_visible(path, locate)
        self.driver.find_element(path, locate).send_keys(values)

    def wait_until_element_is_visible(self, by, locate, time: int = 15):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.visibility_of_element_located((by, locate)))

    def assertion(self, path, error_path):
        self.wait_until_element_is_visible(path, error_path)
        return self.find(path, error_path).text

    # def message(self, error_path, locate):
    #     self.wait_until_element_is_visible(error_path, locate)
    #     return self.find(By.XPATH, error_path).text

    def tear_down(self):
        self.driver.quit()

    def alert_ok_button(self, popup, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.alert_is_present())

        alert = self.driver.switch_to.alert
        assert popup in alert.text
        alert.accept()

    def color_check_up(self, by, locate):
        category_color = self.find(by, locate).value_of_css_property('background-color')
        category_color = Color.from_string(category_color).hex
        print(category_color)

    # def scroll_bar(self, by, locate):
    #     self.wait_until_element_is_visible(by, locate)
    #     self.driver.execute_script("window.scrollBy(0, Document.body.scrollHeight)")


