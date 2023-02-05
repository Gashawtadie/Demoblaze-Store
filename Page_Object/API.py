import allure
import requests
import pytest
from Locators.all_locators import LocatoresBlaze


class TestApi(LocatoresBlaze):
    @allure.description('API test for Login button using get ')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_page(self):
        req = requests.get(self.SIGNIN_URL)
        view_source = req.json()
        status = req.status_code
        time = req.elapsed.total_seconds()

        for i, response in enumerate(req.history, 1):
            print(i, response.url)
        print(req.status_code, req.url)

        required = req.is_permanent_redirect
        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200
        assert time < 10
        assert required == False

    @allure.description('API test for logout button using get')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_page(self):
        reque = requests.get(self.LOGOUT_URL)
        view_source = reque.json()
        status = reque.status_code
        time = reque.elapsed.total_seconds()
        required = reque.is_permanent_redirect
        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200 <= status <= 205
        assert time < 10
        assert required == False

    @allure.description('API test for signup button using get')
    @allure.step
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup_page(self):
        request = requests.get(self.SIGNUP_BTN, self.PAYLOAD)
        view_source = request.json()
        status = request.status_code
        time = request.elapsed.total_seconds()
        required = request.is_permanent_redirect
        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200 <= status <= 205
        assert time < 10
        assert required == False

    @allure.description('API test for About us button using get')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_about_page(self):
        request = requests.get(self.ABOUT_API_URL)
        view_source = request.json()
        status = request.status_code
        time = request.elapsed.total_seconds()
        required = request.is_permanent_redirect
        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200 <= status <= 205
        assert time < 10
        assert required == False


    @allure.description('Test sign up with invalid credentials')
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page(self):
        request = requests.get(self.LOGOUT_URL, self.LOGOUT_DATA)
        view_source = request.json()
        status = request.status_code
        time = request.elapsed.total_seconds()
        required = request.is_permanent_redirect
        print(f"view source = {view_source}\nThe status code is = {status}\nIt takes  {time} seconds\n{required}")
        assert 200 <= status <= 205
        assert time < 10
        assert required == False
