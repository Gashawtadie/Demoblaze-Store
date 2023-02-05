import time

import pytest
from selenium.webdriver.common.by import By
from Base_Page.base_pages import BasePages
from Locators.all_locators import LocatoresBlaze


class TestsAddToCart(BasePages, LocatoresBlaze):
    def add_product(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.LAPTOPS_PATH)
        self.click(By.XPATH, self.MACBOOK_PATH)
        assert self.assertion(By.XPATH, self.product_title) == "MacBook Pro"
        assert self.assertion(By.XPATH, self.PRICE_MAC) == "$1100 *includes tax"
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
        assert self.assertion(By.XPATH, self.THANKYOU_PATH) == "Thank you for your purchase!"

    def cart_color(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.CART_PATH)
        backround_color = self.color_check_up(By.XPATH, self.PLACE_OREDR)
        if backround_color == "#449d44":
            print("color passed")
        else:
            print(backround_color)

    def cart_close_button(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.SONY_VAIO)
        self.click(By.XPATH, self.ADD_CART)
        self.alert_ok_button("Product added")
        self.click(By.XPATH, self.CART_PATH)
        self.click(By.XPATH, self.PLACE_OREDR)
        self.fields(By.XPATH, self.NAME, "one love")
        self.fields(By.XPATH, self.COUNTRY, "israel")
        self.fields(By.XPATH, self.CITY, "Beersheva")
        self.fields(By.XPATH, self.CREDIT_CARD, "123456789987654")
        self.fields(By.XPATH, self.MONTH, "02/01")
        self.fields(By.XPATH, self.YEAR, "2023")
        self.click(By.XPATH, self.CLOSE)

    def price_with_tax(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.PHONE_PATH)
        self.click(By.XPATH, self.IPHONE_PATH)
        assert self.assertion(By.XPATH, self.IPHONE_PRICE) == "$790 *includes tax"
        self.click(By.XPATH, self.ADD_CART)

    def delete_product(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.LAPTOPS_PATH)
        self.click(By.XPATH, self.MACBOOK_PATH)
        self.click(By.XPATH, self.ADD_CART)
        self.alert_ok_button("Product added")
        self.click(By.XPATH, self.CART_PATH)
        self.click(By.XPATH, self.DELETE_PRODUCT)

    def scroll_page(self):
        self.setup_demoblaze()
        self.driver.execute_script("window.scrollBy(0, 100);")
        self.click(By.XPATH, self.NEXT_SCROLL)
        self.click(By.XPATH, self.PREVIOUS_SCROLL)

    def cart_X_close_btn(self):
        self.setup_demoblaze()
        self.click(By.XPATH, self.SONY_VAIO)
        self.click(By.XPATH, self.ADD_CART)
        self.alert_ok_button("Product added")
        self.click(By.XPATH, self.CART_PATH)
        self.click(By.XPATH, self.PLACE_OREDR)
        self.click(By.XPATH, self.X_PLACE_ORDER)

