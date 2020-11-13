import datetime
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import LOGINLocators
from pages.locators import DashboardLocators
from pages.locators import GmailLocators
from pages.locators import RegistrationLocators
from pages.locators import NEW_ONBOARDING_Locators
from pages.locators import LOGIN_PAGELocators
from pages.locators import CLIENT_MANAGMENT_Locators
from selenium.webdriver.support.ui import Select




class Client_Managment(BasePage ):
    CHECKER_TIMEOUT = 20

    def login_how_client(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        def _doing(_wait_page, _LOGIN_PAGELocators):
            wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
            self.send_key(wait_page, LOGIN_PAGELocators.EMAIL, "testapiserpwatch@gmail.com")
            self.send_key(wait_page, LOGIN_PAGELocators.PASSWORD, "7mylife3")
            self.click_btn(wait_page, LOGIN_PAGELocators.BUTTON_SIGNIN)
            wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        try:
            _doing(wait_page, LOGIN_PAGELocators)
        except Exception as e:
            print(f"login_how_admin error: {e}")
            self.close_popup()
            _doing(wait_page, LOGIN_PAGELocators)

    def go_to_the_client_managment(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.click_btn(wait_page, DashboardLocators.BUTTON_ACCOUNT_SETTING)

        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.ajax_complete(wait_ajax)
        self.click_btn(wait_ajax, DashboardLocators.BUTTON_CLIENT_MANAGMENT)

    def create_wl(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, CLIENT_MANAGMENT_Locators.EnableWL)
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)
        self.send_key(wait_ajax,CLIENT_MANAGMENT_Locators.INPUT_NAME, "Autotest WL")
        self.send_key(wait_page, CLIENT_MANAGMENT_Locators.INPUT_ADDRESS, "city Kiev, st. Testing 26, fl. 1 ")







