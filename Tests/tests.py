import allure
import pytest
from selenium.webdriver.common.by import By
from Page_Object.contact import TestsContact
from Page_Object.all_pages import TestPages
from Page_Object.add_to_cart import TestsAddToCart
from Page_Object.about_us import TestsAboutUs
from Page_Object.lists_product import TestList


class TestAllPages(TestPages, TestsAddToCart, TestsContact, TestsAboutUs, TestList):
    def object(self):
        tests = TestAllPages()
        return tests

    @allure.description('Test website title is display in home page')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_title(self):
        self.object().title()

    @allure.description('Test background color is verified')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_home_background_color(self):
        self.object().home_background_color()

    @allure.description('Test website logo is display and click the link go to the home page')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip
    def test_web_logo(self):
        self.object().web_logo()

    @allure.description("Next and back buttons tests")
    @allure.severity(allure.severity_level.NORMAL)
    def test_next_and_back(self):
        self.object().next_and_back()

    @allure.description('Test login with valid credentials')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_valid_login(self):
        self.object().valid_login()

    @allure.description('Verify that Test logout is working properly')
    @allure.step
    @pytest.mark.sanity
    @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout(self):
        self.object().logout()

    @allure.description('Test login with valid credentials')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_btn_color(self):
        self.object().login_btn_color()

    @allure.description('Ensure that the process of add to cart works well')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_add_product(self):
        self.object().add_product()

    @allure.description('Test login with invalid password credentials')
    @allure.step
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @pytest.mark.parametrize("username, password, message", [
        ("gashu", "123", "Wrong password."),
        ("xxxx", "123456789", "Wrong password."),
        ("@#$", "123456789", "Wrong password."),
        ("gashu", "asdfg", "Wrong password."),
        ("", "", "Please fill out Username and Password.")])
    def test_negative_scenario(self, username, password, message):
        self.setup_demoblaze()
        self.click(By.XPATH, self.LOGIN_PATH)
        self.fields(By.ID, self.USERNAME_FIELD, username)
        self.fields(By.ID, self.PASSWORD_FIELD, password)
        self.click(By.XPATH, self.LOGIN_BTN)
        self.alert_ok_button(message)

    @allure.description('Test sign up with valid credentials')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_valid_sign_up(self):
        self.object().valid_sign_up()

    @allure.description('Test sign up with invalid credentials')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username, password, message", [
        ("", "123", "Please fill out Username and Password."),
        ("xxxx", "", "Please fill out Username and Password."),
        ("@#$", "@#123", "This user already exist."),
        ("", "", "Please fill out Username and Password.")])
    def test_negative_scenario_signup(self, username, password, message):
        self.setup_demoblaze()
        self.click(By.XPATH, self.SIGNUP)
        self.fields(By.XPATH, self.SIGNUP_USERNAME, username)
        self.fields(By.XPATH, self.SIGNUP_PASSWORD, password)
        self.click(By.XPATH, self.SIGNUP_BTN)
        self.alert_ok_button(message)

    def test_sign_up_color(self):
        self.object().sign_up_color()

    @allure.description('Verify that Test logout is working properly')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_us_positive(self):
        self.object().contact_us()

    @allure.description('Test contact us with different inputs ')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("Email, Contact_name, message",
                             [
                                 ("", "one", "there is bug in contact page please fix it"),
                                 ("123ab@gmail.com", "", "i cant find relevant message"),
                                 ("ab123@gmail.com", "love", ""),
                                 ("", "", "how can i take the path for assertion for invalid login?"),
                                 ("abcd@gmail.com", "", ""),
                                 ("", "onelove", ""),
                                 ("", "", "")])
    def test_contact_us_negative(self, Email, Contact_name, message):
        self.setup_demoblaze()
        self.click(By.XPATH, self.CONTACT_US)
        self.fields(By.ID, self.CONTACT_EMAIL, Email)
        self.fields(By.ID, self.CONTACT_NAME, Contact_name)
        self.fields(By.ID, self.MESSAGE, message)
        self.click(By.XPATH, self.SEND_MESSAGE)
        self.alert_ok_button("Fill the blank ")

    @allure.description('Test about us close button')
    @allure.step
    @pytest.mark.skip
    @allure.severity(allure.severity_level.CRITICAL)
    def test_about_us_close(self):
        self.object().about_us_close()

    @allure.description('Test color of cart place order button')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_color(self):
        self.object().cart_color()


    @allure.description('Test about us x close ')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_about_us_x_close(self):
        self.object().about_us_x_close()

    @allure.description('verify that users can add many products ')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_pro_lists(self):
        self.object().pro_lists()

    @allure.description('verify the x close can close completely')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_close_button(self):
        self.object().cart_close_button()

    @allure.description('ensure that each products prices are with tax')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_price_with_tax(self):
        self.object().price_with_tax()

    @allure.description('verify that the list of product cart can delete ')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_product(self):
        self.object().delete_product()

    @allure.description('verify the home page can scroll from begging to the end')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_scroll_page(self):
        self.object().scroll_page()

    @allure.description('Verify the x close sign can close the cart page only')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_X_close_btn(self):
        self.object().cart_X_close_btn()

    @allure.description('Verify that the fields of place order are should be fill')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("Name, Country, City, Credit_card, Month, Year, message",
                             [("me", "Ethiopia", "Addis Abeba", "", "", "2027", "Please fill out Name and Creditcard."),
                              ("", "", "Beersheva", "987654321123456", "7/6", "2025",
                               "Please fill out Name and Creditcard."),
                              ("", "Ethiopia", "Sheger", "123654789456", "6/8", "2023",
                               "Please fill out Name and Creditcard."),
                              (
                                      "", "israel", "haifa", "123456789321", "4/7", "",
                                      "Please fill out Name and Creditcard."),
                              ("", "israel", "haifa", "123456789321", "", "2028",
                               "Please fill out Name and Creditcard."),
                              ("", "", "", "123456789321", "", "2029", "Please fill out Name and Creditcard."),
                              ("", "", "", "123456789321", "", "2029", "Please fill out Name and Creditcard."),
                              ("", "", "", "123456789321", "5/5", "", "Please fill out Name and Creditcard.")])
    def test_cart_positive(self, Name, Country, City, Credit_card, Month, Year, message):
        self.setup_demoblaze()
        self.click(By.XPATH, self.SONY_VAIO)
        self.click(By.XPATH, self.ADD_CART)
        self.alert_ok_button("Product added")
        self.click(By.XPATH, self.CART_PATH)
        self.click(By.XPATH, self.PLACE_OREDR)
        self.fields(By.XPATH, self.NAME, Name)
        self.fields(By.XPATH, self.COUNTRY, Country)
        self.fields(By.XPATH, self.CITY, City)
        self.fields(By.XPATH, self.CREDIT_CARD, Credit_card)
        self.fields(By.XPATH, self.MONTH, Month)
        self.fields(By.XPATH, self.YEAR, Year)
        self.click(By.XPATH, self.PURCHASE)
        self.alert_ok_button(message)

    @allure.description('Test about us page and check the video is clickable')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_about_us(self):
        self.object().about_us()

    @allure.description('Ensure that the process of add to cart works well')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_add_product(self):
        self.object().add_product()


    @allure.description('Verify the place order field are should be fill and display fill out the fields ')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("Name, Country, City, Credit_card, Month, Year, message",
                             [("love", "", "haifa", "654789123456", "4/5", "2028","Please fill out Name and Creditcard.!"),
                                 ("love", "israel", "", "123456789321", "12/1", "2028",
                                  "Please fill out Name and Creditcard."),
                                 ("peace", "israel", "haifa", "123456789321", "", "2029",
                                  "Please fill out Name and Creditcard."),
                                 ("healthy", "israel", "haifa", "123456789321", "12/7", "",
                                  "Please fill out Name and Creditcard."),
                                 ("love", "", "", "123456789321", "8/9", "2029", "Please fill out Name and Creditcard."),
                                 ("love", "israel", "", "123456789321", "", "2029",
                                  "Please fill out Name and Creditcard.!"),
                                 ("israel", "haifa", "", "123456789321", "", "2029",
                                  "Please fill out Name and Creditcard."),
                                 ("peace", "", "haifa", "123456789321", "7/5", "",
                                  "Please fill out Name and Creditcard."),
                                 ("wealth", "", "haifa", "123456789321", "4/7", "",
                                  "Please fill out Name and Creditcard."),
                                 ("love", "", "haifa", "123456789321", "", "", "Please fill out Name and Creditcard."),
                             ])
    def test_cart_negative(self, Name, Country, City, Credit_card, Month, Year, message):
        self.setup_demoblaze()
        self.click(By.XPATH, self.SONY_VAIO)
        self.click(By.XPATH, self.ADD_CART)
        self.alert_ok_button("Product added")
        self.click(By.XPATH, self.CART_PATH)
        self.click(By.XPATH, self.PLACE_OREDR)
        self.fields(By.XPATH, self.NAME, Name)
        self.fields(By.XPATH, self.COUNTRY, Country)
        self.fields(By.XPATH, self.CITY, City)
        self.fields(By.XPATH, self.CREDIT_CARD, Credit_card)
        self.fields(By.XPATH, self.MONTH, Month)
        self.fields(By.XPATH, self.YEAR, Year)
        self.click(By.XPATH, self.PURCHASE)
        assert self.assertion(By.XPATH, self.THANKYOU_PATH) == message
        self.click(By.XPATH, self.OK)

    @allure.description('Test contact close button ')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_close(self):
        self.object().contact_close()

    @allure.description('Test contact x close')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_x_close(self):
        self.object().contact_x_close()

    @allure.description('Test place order  close button')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_place_order_close(self):
        self.object().place_order_close()

    @allure.description('Test place order x close  ')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_place_order_x_close(self):
        self.object().place_order_x_close()

    @allure.description('Test sign up close button')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_signup_close_btn(self):
        self.object().signup_close_btn()

    @allure.description('Test sign up x close ')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_signup_x_close_btn(self):
        self.object().signup_x_close_btn()

    @allure.description('Test login close ')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_close_btn(self):
        self.object().login_close_btn()

    @allure.description('Test login x close button ')
    @allure.step
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_x_close_btn(self):
        self.object().login_x_close_btn()

    @allure.description('Test logout without login account')
    @allure.step
    @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout_without_login_account(self):
        self.object().logout_without_login_account()


