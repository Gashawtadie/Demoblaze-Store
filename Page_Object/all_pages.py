import time
import requests
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base_Page.base_pages import BasePages
from selenium.webdriver.support import expected_conditions as ec


class TestPages(BasePages):


    def title(self):
        self.setup_demoblaze()
        try:
            assert 'STORE' in self.driver.title
            print("STORE title is verified")
        except:
            print("STORE title is not verified")

    def next_and_back(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.NEX_PICTURES)
        self.click(By.XPATH, self.BACK_PICTURES)

    def home_background_color(self):
        self.setup_demoblaze()
        self.color_check_up(By.XPATH, self.BACKGROUND_COLOR)

    def valid_login(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.LOGIN_PATH)
        self.fields(By.ID, self.USERNAME_FIELD, "gashu")
        self.fields(By.ID, self.PASSWORD_FIELD, "123456789")
        self.click(By.XPATH, self.LOGIN_BTN)
        if self.assertion(By.XPATH, self.ASSERTION_NAME) == 'Welcome gashu':
            print("Success")
        else:
            print("Invalid login")

    def login_btn_color(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.LOGIN_PATH)
        self.color_check_up(By.XPATH, self.LOGIN_BTN)

    def valid_sign_up(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.SIGNUP)
        self.fields(By.XPATH, self.SIGNUP_USERNAME, "one love")
        self.fields(By.XPATH, self.SIGNUP_PASSWORD, "one123")
        self.click(By.XPATH, self.SIGNUP_BTN)

    def sign_up_color(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.SIGNUP)
        self.color_check_up(By.XPATH, self.SIGNUP_BTN)

    def logout_without_login_account(self):
        self.setup_demoblaze()

        try:
            self.click(By.XPATH, self.LOGOUT)
        except TimeoutException:
            print("you should to have login first in order to logout")

    def logout(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.LOGIN_PATH)
        self.fields(By.ID, self.USERNAME_FIELD, "gashu")
        self.fields(By.ID, self.PASSWORD_FIELD, "123456789")
        self.click(By.XPATH, self.LOGIN_BTN)
        self.click(By.XPATH, self.LOGOUT)
