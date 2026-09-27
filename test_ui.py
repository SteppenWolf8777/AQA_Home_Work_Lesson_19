import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have
import allure

LOGIN = "example1200@example.com"
PASSWORD = "123456"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def test_login():
    """Successful authorization to some demowebshop (UI)"""
    with step("Open login page"):
        browser.open("https://demowebshop.tricentis.com/login")

    with step("Fill login form"):
        browser.element("#Email").send_keys(LOGIN)
        browser.element("#Password").send_keys(PASSWORD).press_enter()

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))
