import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Base_Page.base_pages import BasePages


class TestsContact(BasePages):

    def contact_us(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.CONTACT_US)
        self.fields(By.ID, self.CONTACT_EMAIL, "abcdef@gmail.com")
        self.fields(By.ID, self.CONTACT_NAME, "true")
        self.fields(By.ID, self.MESSAGE, "be the beast")
        self.click(By.XPATH, self.SEND_MESSAGE)
        self.alert_ok_button("Thanks for the message!!")

    def contact_close(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.CONTACT_US)
        self.click(By.XPATH, self.CONTACT_CLOSE)

    def contact_x_close(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.CONTACT_US)
        self.click(By.XPATH, self.CONTACT_X_close)

    def place_order_close(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.CART_PATH)
        self.click(By.XPATH, self.PLACE_OREDR)
        self.click(By.XPATH, self.PLACEORDER_CLOSE)

    def place_order_x_close(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.CART_PATH)
        self.click(By.XPATH, self.PLACE_OREDR)
        self.click(By.XPATH, self.PLACE_ORDER_X_CLOSE)

    def signup_close_btn(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.SIGNUP)
        self.click(By.XPATH, self.SIGNUP_CLOSE_BTN)

    def signup_x_close_btn(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.SIGNUP)
        self.click(By.XPATH, self.SIGNUP_X_CLOSE_BTN)

    def login_close_btn(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.LOGIN_PATH)
        self.click(By.XPATH, self.LOGIN_CLOSE)

    def login_x_close_btn(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.LOGIN_PATH)
        self.click(By.XPATH, self.LOGIN_X_CLOSE)

    def web_logo(self):
        self.setup_demoblaze()
        self.click(By.ID, "nava")

    # def test_edge_browser(self):
    #     edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    #     edge.get("https://www.demoblaze.com/index.html")
    #     ki = edge.find_element(By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4/a")
    #     ki.click()
    #








