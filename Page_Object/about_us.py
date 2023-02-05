import time

import pytest
from selenium.webdriver.common.by import By
from Base_Page.base_pages import BasePages


class TestsAboutUs(BasePages):

    def about_us(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.ABOUT)
        self.click(By.XPATH, self.PLAY_BTN)
        self.click(By.XPATH, self.CLOSE_BTN)

    def about_us_close(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.ABOUT)
        self.click(By.XPATH, self.CLOSE_BTN)

    def about_us_x_close(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.ABOUT)
        self.click(By.XPATH, self.X_CLOSE)

