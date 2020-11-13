from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from selenium import webdriver

from pages.locators import DashboardLocators
from pages.locators import CREAT_PROJECT_WINDOWLocators
from pages.locators import DASHBOARD_PROJECT_LEVELLocators
from pages.locators import LOGIN_PAGELocators
from pages.locators import KEYWORD_Level_Locators
from selenium.webdriver.support import expected_conditions as EC

import os
import time

class Add_new_project(BasePage):
    CHECKER_TIMEOUT = 30

    def login_how_client(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        def _doing(_wait_page, _LOGIN_PAGELocators):
            wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
            self.send_key(wait_page, LOGIN_PAGELocators.EMAIL, "qayevheniia@gmail.com")
            self.send_key(wait_page, LOGIN_PAGELocators.PASSWORD, "7mylife3")
            self.click_btn(wait_page, LOGIN_PAGELocators.BUTTON_SIGNIN)
            wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        try:
            _doing(wait_page, LOGIN_PAGELocators)
        except Exception as e:
            print(f"login_how_admin error: {e}")
            self.close_popup()
            _doing(wait_page, LOGIN_PAGELocators)

    def add_project(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, DashboardLocators.ADD_PROJECT)
        self.click_btn(wait_page, CREAT_PROJECT_WINDOWLocators.ICON_FOR_PROJECT)
        self.send_file(wait_page, CREAT_PROJECT_WINDOWLocators.UPLOAD_ICON,
                      (os.getcwd()+"\Batman SVG File Download Batman.png"))
        self.send_key(wait_page, CREAT_PROJECT_WINDOWLocators.NAME_PROJECT, "Project by Autotest")
        self.send_key(wait_page,CREAT_PROJECT_WINDOWLocators.DOMAIN, "serpwatch.io")
        self.send_key(wait_page, CREAT_PROJECT_WINDOWLocators.KEYWORDS, "serpwatch, serp checker")
        self.send_key(wait_page, CREAT_PROJECT_WINDOWLocators.LANGUAGE, "English")
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)
        self.send_key(wait_page, CREAT_PROJECT_WINDOWLocators.FREQUENCY, "Hourly")
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)
        self.click_btn(wait_page, CREAT_PROJECT_WINDOWLocators.SAVE_PROJECT)
        WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

    def find_project_name_keyword_level(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        wait_page.until(
            EC.visibility_of_element_located(DASHBOARD_PROJECT_LEVELLocators.NAME_PROJECT))

    def open_screenshot(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, DASHBOARD_PROJECT_LEVELLocators.FILTER_BY_NAME, "Project by ")
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)

        self.click_js_btn(wait_ajax, DASHBOARD_PROJECT_LEVELLocators.Enter_to_project)
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_js_btn(wait_page, DASHBOARD_PROJECT_LEVELLocators.ENTER_IN_FIRST_KEYWORD)
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, KEYWORD_Level_Locators.CLICK_CHART)
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_js_btn(wait_page, KEYWORD_Level_Locators.SCREENSHOT)


    def delete_new_project(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, DASHBOARD_PROJECT_LEVELLocators.FILTER_BY_NAME, "Project by ")
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)
        time.sleep(1)
        self.click_btn(wait_ajax, DASHBOARD_PROJECT_LEVELLocators.SELECT_ALL)
        self.click_btn(wait_page, DASHBOARD_PROJECT_LEVELLocators.BUTTON_DELETE_SELECT_PROJECT)
        self.click_btn(wait_page, DASHBOARD_PROJECT_LEVELLocators.ACCEPT_DELETE)

    #def set_up_notification(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)


    def add_keywords(self, keyword1):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, DASHBOARD_PROJECT_LEVELLocators.FILTER_BY_NAME, "Project by ")
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)

        self.click_btn(wait_ajax, DASHBOARD_PROJECT_LEVELLocators.Enter_to_project)
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_js_btn(wait_page, DASHBOARD_PROJECT_LEVELLocators.Add_Keyword)
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, DASHBOARD_PROJECT_LEVELLocators.Input_add_keyword, keyword1)
        self.click_btn(wait_page, DASHBOARD_PROJECT_LEVELLocators.Button_save_keyword)

    def edit_project(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, DASHBOARD_PROJECT_LEVELLocators.FILTER_BY_NAME, "Project by ")
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)
        time.sleep(1)

        self.click_btn(wait_ajax, DASHBOARD_PROJECT_LEVELLocators.BUTTON_EDIT_Project)
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, CREAT_PROJECT_WINDOWLocators.ICON_FOR_PROJECT)
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)

        self.click_js_btn(wait_ajax, CREAT_PROJECT_WINDOWLocators.ICON_BUMBLEBEE)

        self.click_btn(wait_page,CREAT_PROJECT_WINDOWLocators.EDIT_NAME_PROJECT)
        self.send_key(wait_page, CREAT_PROJECT_WINDOWLocators.EDIT_NAME_PROJECT, "+1")

        self.click_btn(wait_page, CREAT_PROJECT_WINDOWLocators.BUTTON_CANCEL_COUNTRY)
        self.send_key(wait_page, CREAT_PROJECT_WINDOWLocators.LOCATION, "Ukraine")
        self.click_btn(wait_page, CREAT_PROJECT_WINDOWLocators.CLICK_COUNTRY)
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)

        self.send_key(wait_page, CREAT_PROJECT_WINDOWLocators.FREQUENCY, "Daily")
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)
        self.send_key(wait_page, CREAT_PROJECT_WINDOWLocators.CHOOSE_ENGINE, "bing.com")
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)

        self.click_btn(wait_page, CREAT_PROJECT_WINDOWLocators.LANGUAGE)
        self.send_key(wait_page, CREAT_PROJECT_WINDOWLocators.LANGUAGE, "Ukrainian")
        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)

        self.click_btn(wait_ajax, CREAT_PROJECT_WINDOWLocators.UPDATE_PROJECT)

        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.ajax_complete(wait_ajax)

        self.click_js_btn(wait_ajax, DASHBOARD_PROJECT_LEVELLocators.Enter_to_project)

    def logout_from_app(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.click_btn(wait_page, DashboardLocators.BUTTON_ACCOUNT_SETTING)
        self.click_btn(wait_page, DashboardLocators.BUTTON_LOGOUT)


















