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
from pages.locators import ADMINLocators


class RegisterPage(BasePage ):
    CHECKER_TIMEOUT = 20

    def go_to_registpage(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, RegistrationLocators.GO_TO_THE_REGISTERPAGE)
        self.click_btn(wait_page, RegistrationLocators.CHECKBOX_RULES)

    def register_by_google(self):
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.ajax_complete(wait_ajax)
        self.click_btn(wait_ajax, RegistrationLocators.BY_GOOGLE)

    def login_in_google_account(self, email, password):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.send_key(wait_page, RegistrationLocators.GOOGLE_EMAIL, email)
        self.click_btn(wait_page, RegistrationLocators.BUTTON_NEXT_GOOGLE)
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, RegistrationLocators.GOOGLE_PASSWORD, password)
        self.click_btn(wait_page, RegistrationLocators.BUTTON_NEXT_GOOGLE_PASSWORD)

    def login_by_google(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.click_btn(wait_page, LOGINLocators.LOGIN_BY_GOOGLE)

    def login_by_facebook(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.click_btn(wait_page, LOGINLocators.LOGIN_BY_FACEBOOK)

    def register_by_usually(self, name, email, password, confirmpassword):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, RegistrationLocators.INPUT_NAME, name)
        self.send_key(wait_page, RegistrationLocators.INPUT_EMAIL, email)
        self.send_key(wait_page, RegistrationLocators.INPUT_PASSWORD, password)
        self.send_key(wait_page, RegistrationLocators.INPUT_CONF_PASSWORD, confirmpassword)
        self.click_btn(wait_page, RegistrationLocators.BUTTON_SIGNUP)

    def register_with_plan(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        time.sleep(2)
        self.select(wait_page, RegistrationLocators.CHOOSE_PLAN, "Personal Plan")

        self.click_btn(wait_page, RegistrationLocators.ChANGE_TERMS)
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, RegistrationLocators.SLIDER_PRICING )
        self.click_btn(wait_page,RegistrationLocators.CONFIRM_PLAN)

    def register_by_facebook(self):
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.ajax_complete(wait_ajax)

        self.click_btn(wait_ajax, RegistrationLocators.BY_FACEBOOK)

    def login_in_facebook_account(self, email, password):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.send_key(wait_page, RegistrationLocators.FACEBOOK_EMAIL, email)
        self.send_key(wait_page, RegistrationLocators.FACEBOOK_PASSWORD, password)
        self.click_btn(wait_page, RegistrationLocators.FACEBOOK_BUTTON)

    def find_dashboard(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        def _doing(_wait_page, _DashboardLocators):
            wait_page.until(
            EC.visibility_of_element_located(DashboardLocators.DASHBORDTEXT))

        try:
            _doing(wait_page, DashboardLocators)
        except Exception as e:
            print(f"login_how_admin error: {e}")
            self.close_popup()
            _doing(wait_page, DashboardLocators)

    def login_how_admin(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, LOGINLocators.ENTER_EMAIL, "yevheniia@leanrank.io")
        self.send_key(wait_page, LOGINLocators.ENTER_PASSWORD, "7mylife3")
        self.click_btn(wait_page, LOGINLocators.BUTTON_LOGIN)

    def go_to_the_admin_panel(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        def _doing(_wait_page, _LOGINLocators):
            self.click_btn(_wait_page, _LOGINLocators.GO_ADMIN_PANEL)

        try:
            _doing(wait_page, LOGINLocators)
        except Exception as e:
            print(f"login_how_admin error: {e}")
            self.close_popup()
            _doing(wait_page, LOGINLocators)


    def delete_test_account(self, email):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, LOGINLocators.FIND_ACCOUNT, email)
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)

        self.click_btn(wait_ajax, LOGINLocators.BUTTON_SEARCH)
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_js_btn(wait_page, LOGINLocators.DELETE_TEST_ACCOUNT)
        self.browser.switch_to.alert.accept()

    def new_anboarding(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.select(wait_page, NEW_ONBOARDING_Locators.Profession, "SEO")
        self.select(wait_page, NEW_ONBOARDING_Locators.Company, "SaaS")
        self.select(wait_page, NEW_ONBOARDING_Locators.Employee, "200-1000")
        self.click_btn(wait_page, NEW_ONBOARDING_Locators.Interview_NOTIFICATION)
        self.click_btn(wait_page, NEW_ONBOARDING_Locators.Interview_Frequency)
        self.click_btn(wait_page, NEW_ONBOARDING_Locators.Interview_Competitors)
        self.click_btn(wait_page, NEW_ONBOARDING_Locators.Button_Go_App)

    def forgot_password(self, email):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.click_btn(wait_page,LOGINLocators.FORGOT_PASSWORD)

        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.send_key(wait_page, LOGINLocators.EMAIl_FOR_FORGOT_PASSWORD, email)
        self.click_btn(wait_page, LOGINLocators.BUTTON_SEND_LINK_FOR_PASSWORD)

    def new_password(self, email, password):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        def _doing(_wait_page, _LOGINLocators):
            self.send_key(wait_page,LOGINLocators.EMAIL_FOR_CREAT_NEW_PASS, email)
            self.send_key(wait_page, LOGINLocators.NEW_PASSWORD, password)
            self.send_key(wait_page, LOGINLocators.NEW_CONFIRM_PASSWORD, password)
            time.sleep(1)
            self.click_btn(wait_page, LOGINLocators.BUTTON_RESET_PASSWORD)

        try:
            _doing(wait_page, LOGINLocators)
        except Exception as e:
            print(f"login_how_admin error: {e}")
            self.close_popup()
            _doing(wait_page, LOGINLocators)

    def logout_from_app(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.click_btn(wait_page, DashboardLocators.BUTTON_ACCOUNT_SETTING)
        self.click_btn(wait_page, DashboardLocators.BUTTON_LOGOUT)

    def logout_from_admin(self):
        self.click_js_simple_btn(ADMINLocators.Logout_from_admin)




