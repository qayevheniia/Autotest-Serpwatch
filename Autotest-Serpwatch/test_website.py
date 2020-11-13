import datetime

import pytest

from pages.locators import WebSiteLocators, SlackLocators, Demo_Account
from pages.website import WebSite
import time

import poplib
import re

from email import parser


link = "https://serpwatch.io/"
link2 = "https://serpwatch.io/serp-checker/"
link3 = "https://nichestack.slack.com/archives/GS5GHRT4N"
link4 = (
    "https://app.hubspot.com/login?hubs_signup-url=www.hubspot.com/&hubs_signup-cta=cta--small"
    "&__cf_chl_jschl_tk__=d6a73b3ee2b7571fdc592b6f5ba1599d7a1c791b-1594988385-0-AZ-2jFD5fwztxp82in8tT6LhOPwbyh"
    "LSPstbVKyeKqyopGkI7_DIrEFi99Zx0VKWJwZHyvedkUL5KbTadlsedjZachTe_Lvkz2OBTFLRxS61Xr9BDeTzsrFudOtrRVwnjZ5p879u"
    "DCptNHErndWOVVKo01AWGlI27BQOteJKje7326BhTjJpUU3endK4qb6cQJTnRd548Tf62TieYgcm2qfhrIY-1W1JassLJnAyzVDWbXnoCh"
    "8wOzZT78E4meQuTmmJhC23Nn62fVR6musWiH3Msw3IeHX2xikSJxOwqAek6gIAgh6o69OOewNNeWiCfce0iV1XXcq82hKzmYLKAs08cEiIQ"
    "cRNkYNerX527IHgghz7h0r3q-bhnDSpzKYLUQ7cGKLm8-suKWLWFEdxE3eEW3ALoMgjvU1DUADrk7g4"
)


def test_checker_1_keywords(browser):
    page = WebSite(browser, link)
    browser.maximize_window()
    page.open()

    domain = "https://serpwatch.io/"
    page.fill_in_fields_united_state(domain=domain)

    keyword1 = "serpwatch"
    page.fill_in_keywords_1_keywords(keyword1=keyword1)
    page.check_position_positive()

    assert page.is_element_present_wait(
        *WebSiteLocators.POSITION1
    ), "Position 1 isn't present "


def test_bing_1_keywords(browser):
    page = WebSite(browser, link)
    browser.maximize_window()
    page.open()

    domain = "https://dou.ua/"
    page.fill_in_fields_ukraine(domain=domain)

    keyword1 = "qa manual"
    page.fill_in_keywords_1_keywords(keyword1=keyword1)
    page.check_position_positive()

    assert page.is_element_present_wait(
        *WebSiteLocators.POSITION1
    ), "Position 1 isn't present bing.com dataseo "


def test_checker_5_keywords(browser):
    page = WebSite(browser, link)
    browser.maximize_window()
    page.open()

    domain = "https://serpwatch.io/"
    page.fill_in_fields_united_state(domain)

    keyword1 = keyword2 = keyword3 = keyword4 = keyword5 = "serpwatch"
    page.fill_in_keywords_5_keywords(keyword1, keyword2, keyword3, keyword4, keyword5)

    assert page.is_element_present_wait(
        *WebSiteLocators.POSITION1,
    ), "Position 1 isn't present "
    assert page.is_element_present_wait(
        *WebSiteLocators.POSITION3
    ), "Position 3 isn't present "
    assert page.is_element_present_wait(
        *WebSiteLocators.POSITION4
    ), "Position 4 isn't present "
    assert page.is_element_present_wait(
        *WebSiteLocators.POSITION5
    ), "Position 5 isn't present "


# negative test cases
def test_without_url(browser):
    page = WebSite(browser, link2)
    browser.maximize_window()
    page.open()

    keyword1 = "тестирование"
    page.fill_in_keywords_1_keywords(keyword1)
    page.check_position_positive()

    assert page.is_element_present(
        *WebSiteLocators.MISTAKE_MESSAGE
    ), "Message about mistake isn't presented, but should  be"
    assert (
        page.browser.find_element(*WebSiteLocators.MISTAKE_MESSAGE).text
        == "Domain field is required"
    ), "No domain missing notification"


def test_without_engine(browser):
    page = WebSite(browser, link2)
    browser.maximize_window()
    page.open()

    domain = "https://dou.ua/"
    page.fill_in_fields_germany(domain)

    keyword1 = "тест"
    page.fill_in_keywords_1_keywords(keyword1)
    page.check_position_positive()

    assert page.is_element_present(
        *WebSiteLocators.MISTAKE_MESSAGE
    ), "Message about mistake isn't presented, but should  be"
    assert (
        page.browser.find_element(*WebSiteLocators.MISTAKE_MESSAGE).text
        == "Search engine field is required"
    ), "No engine missing notification"


def test_with_6_keywords(browser):
    page = WebSite(browser, link)
    browser.maximize_window()
    page.open()

    domain = "https://serpwatch.io/"
    page.fill_in_fields_united_state(domain)

    keyword1 = keyword2 = keyword3 = keyword4 = keyword5 = "serpwatch"
    page.fill_in_keywords_5_keywords(keyword1, keyword2, keyword3, keyword4, keyword5)

    page.should_be_message_about_limit()
    assert (
        page.browser.find_element(*WebSiteLocators.MODAL_ICON_ABOUT_LIMIT).text
        == "You cannot add more than 5 keywords per day"
    ), "The error text about the limit isn't presented"


@pytest.mark.skip(reason="Josh asked to remove this test")
def test_full_chat(browser):
    page = WebSite(browser, link2)
    browser.maximize_window()
    page.open()

    page.checked_chat()

    page = WebSite(browser, link3)
    browser.maximize_window()
    page.open()

    page.should_be_message_in_slack()

    page = WebSite(browser, link4)
    browser.maximize_window()
    page.open()

    page.hubspot_mark_closed()

    datetime.datetime.now()
    dateday = datetime.datetime.now().strftime("%Y_%m_%d")
    assert (
        page.browser.find_elements(*SlackLocators.MESSAGE_WITH_DATE)[-2].text == dateday
    ), "Message in slack  isn't presented"


def test_chat_main_page(browser):
    page = WebSite(browser, link)
    browser.maximize_window()
    page.open()
    page.accept_cookies()
    page.checked_icon_chat()

    assert page.browser.find_element_by_css_selector(
        "#hubspot-messages-iframe-container iframe"
    ), "Icon chat isn't present on the main page"

@pytest.mark.green
def test_screenshot(browser):
    page = WebSite(browser, link)
    browser.maximize_window()
    page.open()

    domain = "dou.ua"
    page.fill_in_fields_united_state(domain)
    keyword1 = "тестирование"

    page.fill_in_keywords_1_keywords(keyword1)
    page.check_position_positive()
    page.should_be_clickeble_screenshot()

    assert page.wait_and_click(
        *WebSiteLocators.ICON_SCREENSHOT
    ), "Screenshot isn't clickeble or not present"


def test_icon_with_100(browser):
    page = WebSite(browser, link)
    browser.maximize_window()
    page.open()

    domain = "dou.ua"
    page.fill_in_fields_united_state(domain)

    keyword1 = "тестирование"
    page.fill_in_keywords_1_keywords(keyword1)

    page.check_position_positive()
    page.should_be_icon_with_100()
    assert (
        page.browser.find_element(*WebSiteLocators.POSITION1).text == "100+"
    ), "In the  icon isn't present 100+"

def test_demo_link(browser):
    page = WebSite(browser, link)
    browser.maximize_window()
    page.open()
    page.demo_link()

    assert (
        page.browser.find_element(*Demo_Account.Projects)
    ), "Demo account don't have projects"

    assert (
        page.browser.find_element(*Demo_Account.Free_Trial_Link)
    ), "Don't have START FREE TRIAL link in demo account "

def test_slider(browser):
    page = WebSite(browser,link)
    browser.maximize_window()
    page.open()
    page.check_calculator()

    assert (
        page.browser.find_element(*WebSiteLocators. Amount_Plan).text == "32"
    ), "The amount don't present or another what need"

def test_meeting_chat(browser):
    page = WebSite(browser,link)
    browser.maximize_window()
    page.open()
    page.find_meeting_icon()

    assert (
        page.is_element_present_wait(*WebSiteLocators.Dates_for_meeting)
    ), "The dates for meeting aren't present"














