import pytest

from pages.registration import RegisterPage
from pages.locators import DashboardLocators, RegistrationLocators, LOGINLocators, DASHBOARD_PROJECT_LEVELLocators, \
    Billinglocators
from pages.creating_project import Add_new_project
from pages.test_gmail import MailService
from pages.client_managment import Client_Managment
import time
import datetime
from pages.locators import KEYWORD_Level_Locators



link = "https://app.serpwatch.io/login"


def test_register_google(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()
    page.go_to_registpage()
    page.register_by_google()
    email = "auototestserpwatch@gmail.com"
    password = "7mylife3"
    page.login_in_google_account(email, password)
    page.new_anboarding()

    assert  page.is_element_present_wait(
        *DashboardLocators.DASHBORDTEXT, timeout=10
    ), "Dashboard isn't present (by google)"
    page.logout_from_app()

def test_login_by_google(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()
    page.login_by_google()
    email = "auototestserpwatch@gmail.com"
    password = "7mylife3"
    page.login_in_google_account(email, password)

    assert  page.is_element_present_wait(
        *DashboardLocators.DASHBORDTEXT
    ), "Dashboard isn't present (by google)"
    page.logout_from_app()


def test_delete_google_account(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()

    page.login_how_admin()
    page.go_to_the_admin_panel()
    email = "auototestserpwatch@gmail.com"
    page.delete_test_account(email)

    assert (
            page.browser.find_element(
                *RegistrationLocators.SUCCESS_MESSAGE_ABOUT_DELETE
            ).text
            == "User deleted successfully!"
    ), "No message about success deleted"
    page.logout_from_admin()

@pytest.mark.green
def test_usually_registration(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()

    page.go_to_registpage()
    name = "Test"
    email = "testapiserpwatch@gmail.com"
    password = confirmpassword ="7mylife3"
    page.register_by_usually(name, email, password, confirmpassword)

    assert  page.is_element_present_wait(
        *RegistrationLocators.MESSAGE_SENT_LINK
    ), "No window with Verify Your Email Address"
    time.sleep(1)

@pytest.mark.green
def test_check_verify_email(browser):
    mail_service = MailService(
        user="testapiserpwatch@gmail.com", password="uyixqulqinyfsfly"
    )
    mail_service.find_registration_verify_url()
    page = RegisterPage(browser, mail_service.verify_url)

    browser.maximize_window()
    page.open()
    page.new_anboarding()
    page.find_dashboard()

    assert  page.is_element_present_wait(
        *DashboardLocators.DASHBORDTEXT
    ), "Dashboard isn't present by usually registration"
    page.logout_from_app()

def test_client_managment(browser):
    page = Client_Managment(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_client()
    page.go_to_the_client_managment()
    page.create_wl()

@pytest.mark.green
def test_delete_ussually_account(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_admin()
    page.go_to_the_admin_panel()
    time.sleep(2)
    email = "testapiserpwatch@gmail.com"
    page.delete_test_account(email)

    assert (
            page.browser.find_element(
                *RegistrationLocators.SUCCESS_MESSAGE_ABOUT_DELETE
            ).text
            == "User deleted successfully!"
    ), "No message about success deleted"
    page.logout_from_admin()

@pytest.mark.green
def test_usually_registration_plan(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()
    page.go_to_registpage()
    page.register_with_plan()
    name = "Test"
    email = "testapiserpwatch@gmail.com"
    password = confirmpassword ="7mylife3"
    page.register_by_usually(name, email, password, confirmpassword)

    assert  page.is_element_present_wait(
        *RegistrationLocators.MESSAGE_SENT_LINK
    ), "No window with Verify Your Email Address"
    time.sleep(1)

@pytest.mark.green
def test_check_verify_email_plan(browser):
    mail_service = MailService(
        user="testapiserpwatch@gmail.com", password="uyixqulqinyfsfly"
    )
    mail_service.find_registration_verify_url()
    page = RegisterPage(browser, mail_service.verify_url)

    browser.maximize_window()
    page.open()
    page.new_anboarding()

    assert  page.is_element_present_wait(
        *Billinglocators.Name_page
    ), "The page isn't Billing"
    page.logout_from_app()

@pytest.mark.green
def test_forgot_password(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()
    email = "testapiserpwatch@gmail.com"
    page.forgot_password(email)

    assert  page.is_element_present_wait(
        *LOGINLocators.SUCCES_LINK_FOR_CHANGE_PASSWORD
    ), "Link has been sent! - text isn't present"
    time.sleep(1)

@pytest.mark.green
def test_check_link_for_change_password(browser):
    mail_service = MailService(
        user="testapiserpwatch@gmail.com", password="uyixqulqinyfsfly", pattern="serpwatch.io/password/reset"
    )
    mail_service.find_registration_verify_url()
    page = RegisterPage(browser, mail_service.verify_url)

    browser.maximize_window()
    page.open()
    email = "testapiserpwatch@gmail.com"
    password = "7mylife3"
    page.new_password(email, password)

    assert  page.is_element_present_wait(
        *Billinglocators.Name_page
    ), "The page isn't Billing (test for function (Forgot password)"
    page.logout_from_app()

@pytest.mark.green
def test_delete_ussually_account_plan(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_admin()
    page.go_to_the_admin_panel()
    email = "testapiserpwatch@gmail.com"
    page.delete_test_account(email)

    assert (
            page.browser.find_element(
                *RegistrationLocators.SUCCESS_MESSAGE_ABOUT_DELETE
            ).text
            == "User deleted successfully!"
    ), "No message about success deleted"
    page.logout_from_admin()

def test_registration_facebook(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()

    page.go_to_registpage()
    page.register_by_facebook()
    email = "hristina.nikolovska@leanrank.io"
    password = "d0ntfuckwithus"
    page.login_in_facebook_account(email, password)
    page.new_anboarding()
    page.find_dashboard()

    assert  page.is_element_present_wait(
        *DashboardLocators.DASHBORDTEXT
    ), "Dashboard isn't present by facebook"
    page.logout_from_app()

def test_login_by_facebook(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()
    page.login_by_facebook()
    email = "hristina.nikolovska@leanrank.io"
    password = "d0ntfuckwithus"
    page.login_in_facebook_account(email, password)

    assert  page.is_element_present_wait(
        *DashboardLocators.DASHBORDTEXT
    ), "Dashboard isn't present by facebook"
    page.logout_from_app()


def test_delete_facebook_account(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_admin()
    page.go_to_the_admin_panel()
    email = "hristina.nikolovska@leanrank.io"
    page.delete_test_account(email)

    assert (
            page.browser.find_element(
                *RegistrationLocators.SUCCESS_MESSAGE_ABOUT_DELETE
            ).text
            == "User deleted successfully!"
    ), "No message about success deleted"
    page.logout_from_admin()

def test_registration_facebook_with_plan(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()

    page.go_to_registpage()
    page.register_with_plan()
    page.register_by_facebook()
    email = "hristina.nikolovska@leanrank.io"
    password = "d0ntfuckwithus"
    page.login_in_facebook_account(email, password)
    page.new_anboarding()

    assert  page.is_element_present_wait(
        *Billinglocators.Name_page
    ), "The page isn't Billing"
    page.logout_from_app()


def test_delete_facebook_account_plan(browser):
    page = RegisterPage(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_admin()
    page.go_to_the_admin_panel()
    email = "hristina.nikolovska@leanrank.io"
    page.delete_test_account(email)

    assert (
            page.browser.find_element(
                *RegistrationLocators.SUCCESS_MESSAGE_ABOUT_DELETE
            ).text
            == "User deleted successfully!"
    ), "No message about success deleted"
    page.logout_from_admin()

def test_add_project(browser):
    page = Add_new_project(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_client()
    page.add_project()
    page.find_project_name_keyword_level()

    assert (
            page.browser.find_element(
                *DASHBOARD_PROJECT_LEVELLocators.NAME_PROJECT
            ).text
            == "Project by Autotest"
    ), "No project in dashboard what we created"
#is position presented?
    assert page.is_element_present_wait(
        *DASHBOARD_PROJECT_LEVELLocators.Position_Serpwatch
    ), "Position 1 isn't present (for serpwatch)"

    SV = page.browser.find_element(
                *DASHBOARD_PROJECT_LEVELLocators.Search_Volume
            ).text
#is data from dataseo preesented?
    assert int(SV) > 0, "SV < 0 or isn't presented "

#is right engine dispalyed?
    assert (
            page.browser.find_element(
                *DASHBOARD_PROJECT_LEVELLocators.Engine
            ).text
            =="google.com"
    ), "Wrong engine,  not google"
    page.logout_from_app()


def test_screenshot(browser):
    page = Add_new_project(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_client()
    page.open_screenshot()

    Height = page.browser.find_element(*KEYWORD_Level_Locators.SCREENSHOT).size['height']

    assert (Height) > 5, "Height < 5 Pixel or isn't presented "



def test_add_keywords(browser):
    page = Add_new_project(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_client()
    keyword1= "test, seo"
    page.add_keywords(keyword1)

    assert page.is_element_present_wait(
        *DASHBOARD_PROJECT_LEVELLocators.Position_Serpwatch_for_invalid_keyword
    ), "Position 100+ isn't present (for serpwatch)"
    page.logout_from_app()


def test_add_long_keyword_50_characters(browser):
    page = Add_new_project(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_client()
    keyword = "For check long keywords up to 50 separated by comm"
    page.add_keywords(keyword)

    assert page.is_element_present_wait(
        *DASHBOARD_PROJECT_LEVELLocators.SUCCESS_MESSAGE_ABOUT_ADD_Keywords
    ), "Keyword with 50 characters isn't added"
    page.logout_from_app()


#negative test for long keyword more then 50 characters

def test_add_long_keyword_51_characters(browser):
    page = Add_new_project(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_client()
    keyword = "For check long keywords up to 51 separated by comma"
    page.add_keywords(keyword)

    assert page.is_element_present_wait(
        *DASHBOARD_PROJECT_LEVELLocators.UNSUCCESS_MESSAGE_FOR_lONG_KEYWORD
    ), "Keyword with 51 characters is added"
    page.logout_from_app()


def test_add_keywords_kirilica(browser):
    page = Add_new_project(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_client()
    keyword1= "тестирование"
    page.add_keywords(keyword1)

    assert page.is_element_present_wait(
        *DASHBOARD_PROJECT_LEVELLocators.Position_Serpwatch_for_invalid_keyword
    ), "Position 100+ isn't present (for serpwatch)"
    page.logout_from_app()


def test_edit_project(browser):
    page = Add_new_project(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_client()
    page.edit_project()

    assert page.is_element_present_wait(*DASHBOARD_PROJECT_LEVELLocators.ENGINE_BING), "Wrong engine,  not bing.com"

    assert page.is_element_present(*DASHBOARD_PROJECT_LEVELLocators.FLAG_UKRAINE), "Wrong country, not Ukraine"

    assert page.is_element_present(*DASHBOARD_PROJECT_LEVELLocators.LANGUAGE_UKRANIAN), "Wrong language, not ukranian"

    assert page.is_element_present(*DASHBOARD_PROJECT_LEVELLocators.HOURLY_UPDATE), "Wrong frequency, not hourly"
    page.logout_from_app()


def test_delete_new_projects(browser):
    page = Add_new_project(browser, link)
    browser.maximize_window()
    page.open()
    page.login_how_client()
    page.delete_new_project()
    assert page.is_element_present_wait(
                *DASHBOARD_PROJECT_LEVELLocators.SUCCESS_MESSAGE_ABOUT_DELETE_Project
            ), "No message about success deleted"
    page.logout_from_app()





















