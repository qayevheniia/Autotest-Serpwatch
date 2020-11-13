import datetime
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import HubspotLocators
from pages.locators import SlackLocators, Demo_Account
from pages.locators import WebSiteLocators




class WebSite(BasePage):
    CHECKER_TIMEOUT = 50

    def fill_in_fields_united_state(self, domain):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, WebSiteLocators.GO_TO_CHECKER)
        self.send_key(wait_page, WebSiteLocators.DOMAIN_NAME, domain)

    def fill_in_fields_ukraine(self, domain):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, WebSiteLocators.GO_TO_CHECKER)
        self.send_key(wait_page, WebSiteLocators.DOMAIN_NAME, domain)
        self.send_key(wait_page, WebSiteLocators.COUNTRY, "Ukraine")

        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.ajax_complete(wait_ajax)
        self.click_btn(wait_ajax, WebSiteLocators.ENGINE)
        self.change_style(
            WebSiteLocators.ENGINE_SELECT_ELEMENT, "width: auto;height: auto;"
        )
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_js_btn(wait_page, WebSiteLocators.ENGINE_BING_UKRAINE)

    def fill_in_keywords_1_keywords(self, keyword1):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, WebSiteLocators.KEYWORD1, keyword1)

    def fill_in_keywords_5_keywords(
        self, keyword1, keyword2, keyword3, keyword4, keyword5
    ):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, WebSiteLocators.KEYWORD1, keyword1)
        self.click_btn(wait_page, WebSiteLocators.CHECK_KEYWORDS)

        self.send_key(wait_page, WebSiteLocators.KEYWORD2, keyword2)
        self.click_js_btn(wait_page, WebSiteLocators.CHECK_KEYWORDS)

        self.send_key(wait_page, WebSiteLocators.KEYWORD3, keyword3)
        self.click_js_btn(wait_page, WebSiteLocators.CHECK_KEYWORDS)

        self.click_js_btn(wait_page, WebSiteLocators.ADD_KEYWORD)
        self.send_key(wait_page, WebSiteLocators.KEYWORD4, keyword4)
        self.click_js_btn(wait_page, WebSiteLocators.CHECK_KEYWORDS)

        self.click_js_btn(wait_page, WebSiteLocators.ADD_KEYWORD)
        self.send_key(wait_page, WebSiteLocators.KEYWORD5, keyword5)
        self.click_js_btn(wait_page, WebSiteLocators.CHECK_KEYWORDS)

    def check_position_positive(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_js_btn(wait_page, WebSiteLocators.CHECK_KEYWORDS)

    def should_be_message_about_mistake(self):
        self.browser.find_element(*WebSiteLocators.CHECK_KEYWORDS).click()

    def fill_in_fields_germany(self, domain):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.send_key(wait_page, WebSiteLocators.DOMAIN_NAME, domain)
        self.click_btn(wait_page, WebSiteLocators.COUNTRY)
        self.send_key(wait_page, WebSiteLocators.COUNTRY, "Germany")

        wait_ajax = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.ajax_complete(wait_ajax)

    def checked_icon_chat(self, timeout=20):
        self.browser.implicitly_wait(timeout)

    # removed this test from main test (asked Josh about this)
    def checked_chat(self, timeout=20):
        self.browser.implicitly_wait(timeout)
        iframe = self.browser.find_element_by_css_selector(
            "#hubspot-messages-iframe-container iframe"
        )
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame(iframe)
        icon_chat = self.browser.find_element(*WebSiteLocators.ICON_CHAT)
        self.browser.execute_script("arguments[0].click();", icon_chat)
        self.browser.find_element(*WebSiteLocators.CHAT_SOMETHING_ELSE).click()
        time.sleep(5)
        self.browser.find_element(*WebSiteLocators.CHAT_INPUT_FIELD).send_keys(
            "Autotest"
        )
        self.browser.find_element(*WebSiteLocators.CHAT_SEND_BUTTON).click()
        time.sleep(5)  # need to change in wait active
        self.browser.find_element(*WebSiteLocators.CHAT_SELECT_AMOUNT_TEAM).click()
        time.sleep(5)  # need to change in wait active
        self.browser.find_element(*WebSiteLocators.CHAT_TYPE_TEAM).click()
        time.sleep(5)  # need to change in wait active
        self.browser.find_element(*WebSiteLocators.CHAT_INPUT_FIELD).send_keys(
            "auototestserpwatch@gmail.com"
        )
        self.browser.find_element(*WebSiteLocators.CHAT_SEND_BUTTON).click()
        time.sleep(5)
        datetime.datetime.now()
        date_string = datetime.datetime.now().strftime("%Y_%m_%d")
        self.browser.find_element(*WebSiteLocators.CHAT_INPUT_FIELD).send_keys(
            date_string
        )
        self.browser.find_element(*WebSiteLocators.CHAT_SEND_BUTTON).click()
        self.browser.implicitly_wait(timeout)

    def should_be_message_in_slack(self, timeout=20):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)
        self.browser.implicitly_wait(timeout)

        self.send_key(wait_page, SlackLocators.SLACK_EMAIL, "motytskaya@gmail.com")
        self.send_key(wait_page, SlackLocators.SLACK_PASSWORD, "7mylife3")
        self.click_btn(wait_page, SlackLocators.SLACK_SIGNIN)

        self.browser.implicitly_wait(timeout)

        last_message = self.browser.find_elements(*SlackLocators.FIND_LAST_MESSAGE)[-1]
        self.browser.execute_script("arguments[0].click();", last_message)
        self.click_btn(wait_page, SlackLocators.SECOND_WORKSPACE)

        self.browser.implicitly_wait(timeout)

    def should_be_message_about_limit(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, WebSiteLocators.ADD_KEYWORD)
        wait_page.until(
            EC.visibility_of_element_located(WebSiteLocators.MODAL_ICON_ABOUT_LIMIT)
        )

    def hubspot_mark_closed(self, timeout=20):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.browser.implicitly_wait(timeout)

        self.send_key(wait_page, HubspotLocators.USERNAME, "qayevheniia@gmail.com")
        self.send_key(wait_page, HubspotLocators.PASSWORD, "Mzhenya1987")

        self.click_btn(wait_page, HubspotLocators.BUTTON)
        self.click_btn(wait_page, HubspotLocators.CONVERSATIONS)
        self.click_btn(wait_page, HubspotLocators.INBOX)
        self.click_btn(wait_page, HubspotLocators.FIND_AUTOTEST)
        self.click_btn(wait_page, HubspotLocators.MARK_CLOSED)

    def should_be_clickeble_screenshot(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, WebSiteLocators.CHECK_KEYWORDS)

    def should_be_icon_with_100(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.text_change(wait_page, WebSiteLocators.POSITION1)

    def demo_link(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, WebSiteLocators.Demo_link)

        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, Demo_Account.Modal_Icon_Welcome)

    def check_calculator(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, WebSiteLocators.Pricing_page)

        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_btn(wait_page, WebSiteLocators.five_th_keywords)

    def find_meeting_icon(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.activate_new_tab(self, wait_page, WebSiteLocators.Icon_meeting)


    def accept_cookies(self):
        wait_page = WebDriverWait(self.browser, self.CHECKER_TIMEOUT)

        self.click_js_btn(wait_page, WebSiteLocators.Accept_cookies)





















