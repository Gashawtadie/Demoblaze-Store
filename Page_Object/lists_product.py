import time

import pytest
from selenium.webdriver.common.by import By

from Base_Page.base_pages import BasePages


class TestList(BasePages):
    def pro_lists(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.PHONE_PATH)
        self.click(By.XPATH, self.HTC_PHONE_PATH)
        if self.assertion(By.XPATH, self.HTC_NAME_PATH) == "HTC One M9" and self.assertion(By.XPATH,
                                                                                           self.HTC_PRICE) == "$700 *includes tax":
            self.click(By.XPATH, self.ADD_CART)
        else:
            quit()
        self.alert_ok_button("Product added")
        self.click(By.XPATH, self.MAIN_HOME)
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.LAPTOPS_PATH)
        self.click(By.XPATH, self.MACBOOK_PRO)
        if self.assertion(By.XPATH, self.MAC_NAME) == "MacBook Pro" and self.assertion(By.XPATH,
                                                                                       self.MAC_PRICE) == "$1100 *includes tax":
            self.click(By.XPATH, self.ADD_CART)
        else:
            quit()
        self.alert_ok_button("Product added")
        self.click(By.XPATH, self.MAIN_HOME)
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.MONITOR)
        self.click(By.XPATH, self.APPLE_MONITOR)
        if self.assertion(By.XPATH, self.APPLE_NAME_PATH) == "Apple monitor 24" and self.assertion(By.XPATH,
                                                                                                   self.APPLE_PRICE_PATH) == "$400 *includes tax":
            self.click(By.XPATH, self.ADD_CART)
        else:
            print("assertion not successful")
        self.alert_ok_button("Product added")
        self.click(By.XPATH, self.CART_PATH)
        self.click(By.XPATH, self.PLACE_OREDR)
        self.fields(By.XPATH, self.NAME, "gashu")
        self.fields(By.XPATH, self.COUNTRY, "Israel")
        self.fields(By.XPATH, self.CITY, "Beersheva")
        self.fields(By.XPATH, self.CREDIT_CARD, "1234567899874563")
        self.fields(By.XPATH, self.MONTH, "01/02")
        self.fields(By.XPATH, self.YEAR, "2025")
        self.click(By.XPATH, self.PURCHASE)
        assert self.assertion(By.XPATH, self.THANKYOU_PATH) == "Thank you for your purchase!"
        self.click(By.XPATH, self.OK)

    #def test_validity(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.HTC_PHONE_PATH)
        self.click(By.XPATH, self.ADD_CART)
        self.alert_ok_button("Product added")
        self.click(By.XPATH, self.CART_PATH)
        self.click(By.XPATH, self.PLACE_OREDR)
        self.fields(By.XPATH, self.NAME, "gashu")
        self.fields(By.XPATH, self.COUNTRY, "Israel")
        self.fields(By.XPATH, self.CITY, "Beersheva")
        self.fields(By.XPATH, self.CREDIT_CARD, "1234567899874563")
        self.fields(By.XPATH, self.MONTH, "01/02")
        self.fields(By.XPATH, self.YEAR, "2025")
        self.click(By.XPATH, self.PURCHASE)
        ul = "p"
        pri = "p"
        new = self.driver.find_element(By.TAG_NAME, ul)
        ow = new.find_elements(By.TAG_NAME, pri)
        for n in ow:
            if n == "Card Number: 1234567899874563":
                self.click(By.XPATH, self.OK)
            else:
                break

    # def test_scroll(self):
    #     self.setup_demoblaze()
    #     self.driver.execute_script("window.scrollBy(0, 100)")
    #


