from selenium.webdriver.common.by import By


class WebSiteLocators:
    GO_TO_CHECKER = (
        By.CSS_SELECTOR,
                     "#menu-item-2832 >.nav-link")
    DOMAIN_NAME = (
        By.CSS_SELECTOR,
                   ".form-control.ff-sfpro.input-domain")
    COUNTRY = (
        By.CSS_SELECTOR,
               "#country-selector")
    KEYWORD1 = (
        By.CSS_SELECTOR,
                ".keywords-block .checker_keyword:nth-child(1) input")
    KEYWORD2 = (
        By.CSS_SELECTOR,
                ".keywords-block .checker_keyword:nth-child(2) input")
    KEYWORD3 = (
        By.CSS_SELECTOR,
                ".keywords-block .checker_keyword:nth-child(3) input")
    ADD_KEYWORD = (
        By.CSS_SELECTOR,
                   "button.add-keyword")
    KEYWORD4 = (
        By.CSS_SELECTOR,
                ".keywords-block .checker_keyword:nth-child(4) input")
    KEYWORD5 = (
        By.CSS_SELECTOR,
                ".keywords-block .checker_keyword:nth-child(5) input")
    CHECK_KEYWORDS = (
        By.CSS_SELECTOR,
                      "#check-all.btn")
    ENGINE = (
        By.CSS_SELECTOR,
        ".selectric-wrapper.selectric-form-control.selectric-search-engine",
    )
    LANGUAGE = (
        By.CSS_SELECTOR,
        ".selectric-wrapper.selectric-form-control.selectric-language",
    )
    ENGINE_SELECT_ELEMENT = (
        By.CSS_SELECTOR,
        ".selectric-wrapper.selectric-form-control.selectric-search-engine > .selectric-items",
    )
    LANGUAGE_SELECT_ELEMENT = (
        By.CSS_SELECTOR,
        ".selectric-wrapper.selectric-form-control.selectric-language > .selectric-items",
    )
    ENGINE_BING_UKRAINE = (
        By.CSS_SELECTOR,
        ".selectric-scroll > ul > li.last")
    ENGINE_LANGUAGE = (
        By.CSS_SELECTOR,
        ".selectric-scroll > ul > li.last")
    POSITION1 = (
        By.CSS_SELECTOR,
        "div:nth-child(1) >.form-row>.col-8.col-sm-8 >.input-group>.input-group-append>span",
    )
    POSITION2 = (
        By.CSS_SELECTOR,
        "div:nth-child(2) >.form-row>.col-8.col-sm-8 >.input-group>.input-group-append>span",
    )
    POSITION3 = (
        By.CSS_SELECTOR,
        "div:nth-child(3) >.form-row>.col-8.col-sm-8 >.input-group>.input-group-append>span",
    )
    POSITION4 = (
        By.CSS_SELECTOR,
        "div:nth-child(4) >.form-row>.col-8.col-sm-8 >.input-group>.input-group-append>span",
    )
    POSITION5 = (
        By.CSS_SELECTOR,
        "div:nth-child(5) >.form-row>.col-8.col-sm-8 >.input-group>.input-group-append>span",
    )
    MISTAKE_MESSAGE = (By.CSS_SELECTOR, "p.error")
    DELETE_KEYWORD1 = (
        By.CSS_SELECTOR,
        "div:nth-child(1) > div > div.col-4 > button.btn.btn-br.ff-sfpro.btn-close>img",
    )
    ICON_CHAT = (
        By.CSS_SELECTOR,
        "button.IconLauncher__BaseLauncher-wl773y-0")
    CHAT_SOMETHING_ELSE = (
        By.CSS_SELECTOR,
        "button:nth-child(5)> span")
    CHAT_INPUT_FIELD = (
        By.CSS_SELECTOR,
        ".widget-textarea")
    CHAT_SEND_BUTTON = (
        By.CSS_SELECTOR,
        ".chat-send-button")
    CHAT_SELECT_AMOUNT_TEAM = (
        By.CSS_SELECTOR,
        ".align-center> button:nth-child(1)")
    CHAT_TYPE_TEAM = (
        By.CSS_SELECTOR,
        ".align-center> button:nth-child(2)")
    MODAL_ICON_ABOUT_LIMIT = (
        By.XPATH,
        '//p[contains(text(), "5 keywords")]')
    ICON_SCREENSHOT = (
        By.CSS_SELECTOR,
        "button.btn.btn-br.ff-sfpro.btn-gl")
    SCREENSHOT = (
        By.CSS_SELECTOR,
        ".engin-scrin > img")
    Demo_link = (
        By.XPATH,
        '//a[contains(text(), "Live Demo")]')
    Free_Trial_link = (
        By.XPATH,
        '//a[contains(text(), "Free Trial")]')
    Pricing_page = (
        By.XPATH,
        '//a[contains(text(),"Pricing")]')
    Slider_Calculator = (
        By.CSS_SELECTOR,
        ".ui-slider-range.ui-corner-all.ui-widget-header.ui-slider-range-min")
    Amount_Plan = (
        By.CSS_SELECTOR,
        "#annualPrice")
    five_th_keywords = (
        By.CSS_SELECTOR,
        '#pricingSlider .ui-slider-pip-3')
    Icon_meeting = (
        By.CSS_SELECTOR,
        ".home > div.demo-block.schedule")
    Dates_for_meeting = (
        By.CSS_SELECTOR,
        "#bsb-1")
    Time_for_meeting = (By.CSS_SELECTOR, '#duration-select > button:nth-child(1)')
    Accept_cookies = (By.XPATH,'//a[contains(text(),"Accept cookies")]')

class Demo_Account:
    Modal_Icon_Welcome = (By.XPATH, '//button[contains(text(), "Close")]')
    Projects = (By.CSS_SELECTOR, ".projectLink")
    Free_Trial_Link = (By.XPATH, '//button[contains(text(), "Start Free Trial")]')

class RegistrationLocators:
    GO_TO_THE_REGISTERPAGE = (By.CSS_SELECTOR, ".btn.btn-rounded.btn-register")
    CHECKBOX_RULES = (By.CSS_SELECTOR, "label.custom-control-label")
    BY_GOOGLE = (By.XPATH, '//button[contains(text(), " Sign up with Google")]')
    BY_FACEBOOK = (By.CSS_SELECTOR, "#facebook")
    GOOGLE_EMAIL = (By.CSS_SELECTOR, "#identifierId")
    GOOGLE_PASSWORD = (By.CSS_SELECTOR, "#password > div> div > div> input")
    BUTTON_NEXT_GOOGLE = (By.CSS_SELECTOR, "#identifierNext")
    BUTTON_NEXT_GOOGLE_PASSWORD = (By.CSS_SELECTOR, "#passwordNext")
    FACEBOOK_EMAIL = (By.CSS_SELECTOR, "#email")
    FACEBOOK_PASSWORD = (By.CSS_SELECTOR, "#pass")
    FACEBOOK_BUTTON = (By.CSS_SELECTOR, "#loginbutton")
    FACEBOOK_ACCEPT = (By.XPATH, '//button[contains(text(), "Continue as Niche")]')
    SUCCESS_MESSAGE_ABOUT_DELETE = (By.CSS_SELECTOR, "div.toast.toast-success")
    INPUT_NAME = (By.CSS_SELECTOR, "#name")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")
    INPUT_CONF_PASSWORD = (By.CSS_SELECTOR, "#password_confirmation")
    BUTTON_SIGNUP = (By.CSS_SELECTOR, "#register")
    MESSAGE_SENT_LINK = (By.XPATH, '//b[contains(text(), "testapiserpwatch@gmail.com" )]')
    CHOOSE_PLAN = (By.CSS_SELECTOR, '#plan')
    ChANGE_TERMS = (By.CSS_SELECTOR, "#popup-personal")
    SLIDER_PRICING = (By.CSS_SELECTOR, "#pricingSlider .ui-slider-pip-3")
    CONFIRM_PLAN = (By.CSS_SELECTOR, "#confirm-plan")
    FACEBOOK_ACCEPT_COOKIE = (By.XPATH,'//button[contains(text(),"Accept All")]')

class GmailLocators:
    LAST_WELCOME_MESSAGE = (
        By.XPATH,
        '//span[contains(text(), "Welcome to SerpWatch")]',
    )
    VERIFY_EMAIL = (By.XPATH, '//a[contains(text(), "Verify Email Address" )]')


class LOGINLocators:
    ENTER_EMAIL = (By.CSS_SELECTOR, "#email")
    ENTER_PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "#login")
    GO_ADMIN_PANEL = (By.CSS_SELECTOR, ".icon-serp-arrow-left.ic-1x5.ic-white")
    FIND_ACCOUNT = (By.CSS_SELECTOR, "#search-box")
    BUTTON_SEARCH = (
        By.CSS_SELECTOR,
        "form.form-inline.search-form.float-left > button",
    )
    DELETE_TEST_ACCOUNT = (By.XPATH, '//button[contains(text(), " Delete")]')
    LOGIN_BY_GOOGLE = (By.XPATH, '//button[contains(text(), " Sign in with Google")]')
    LOGIN_BY_FACEBOOK = (By.XPATH, '//button[contains(text(), "Sign in with Facebook")]')
    FORGOT_PASSWORD = (By.XPATH,'//a[contains(text(), "Forgot your password?")]')
    EMAIl_FOR_FORGOT_PASSWORD = (By.CSS_SELECTOR,"#email")
    BUTTON_SEND_LINK_FOR_PASSWORD = (By.CSS_SELECTOR, "#submitbtn")
    SUCCES_LINK_FOR_CHANGE_PASSWORD = (By.XPATH, '//h3[contains(text(), "Link has been sent!")]')
    EMAIL_FOR_CREAT_NEW_PASS = (By.CSS_SELECTOR, "#email")
    NEW_PASSWORD = (By.CSS_SELECTOR, "#password")
    NEW_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#password-confirm")
    BUTTON_RESET_PASSWORD = (By.XPATH, '//button[contains(text(), "Reset Password")]')

class SlackLocators:
    SLACK_URL = (By.CSS_SELECTOR, "#domain")
    SLACK_BUTTON_CONTINUE = (By.CSS_SELECTOR, "#submit_team_domain")
    SLACK_EMAIL = (By.CSS_SELECTOR, "#email")
    SLACK_PASSWORD = (By.CSS_SELECTOR, "#password")
    SLACK_SIGNIN = (By.CSS_SELECTOR, "#signin_btn")
    FIND_LAST_MESSAGE = (By.CSS_SELECTOR, ".c-link.c-message__reply_count")
    SECOND_WORKSPACE = (
        By.CSS_SELECTOR,
        ".p-workspace-layout >.p-workspace__secondary_view",
    )
    MESSAGE_WITH_DATE = (By.CSS_SELECTOR, ".c-message_kit__text")


class HubspotLocators:
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON = (By.CSS_SELECTOR, "#loginBtn")
    CONVERSATIONS = (By.CSS_SELECTOR, "#nav-primary-conversations-branch")
    INBOX = (By.CSS_SELECTOR, "#nav-secondary-inbox")
    FIND_AUTOTEST = (By.XPATH, '//span[contains(text(), "Autotest")]')
    MARK_CLOSED = (By.XPATH, '//i18n-string[contains(text(), "Mark as closed")]')


class DashboardLocators:
    DASHBORDTEXT = (By.XPATH, '//h1[contains(text(),"Dashboard")]')
    ADD_PROJECT = (By.CSS_SELECTOR, "#projectDefault")
    NAME_PROJECT_BY_AUTOTEST = (By.XPATH, '//a[contains(text(),"Project by Autotest")]')
    BUTTON_ACCOUNT_SETTING = (By.CSS_SELECTOR, "button.btn-floating-account")
    BUTTON_LOGOUT = (By.XPATH, '//a[contains(text(),"Logout")]')
    BUTTON_CLIENT_MANAGMENT = (By.XPATH,'//a[contains(text(),"Client Management")]')

class LOGIN_PAGELocators:
    EMAIL = (By.CSS_SELECTOR,"#email")
    PASSWORD = (By.CSS_SELECTOR,"#password")
    BUTTON_SIGNIN = (By.CSS_SELECTOR,"#login")

class CREAT_PROJECT_WINDOWLocators:
    ICON_FOR_PROJECT = (By.CSS_SELECTOR,"#projectImage")
    UPLOAD_ICON = (By.CSS_SELECTOR,"#inputImageFromComputer")
    NAME_PROJECT = (By.CSS_SELECTOR,"#step2")
    DOMAIN = (By.CSS_SELECTOR, "#step3")
    KEYWORDS = (By.CSS_SELECTOR, "#keywords_name")
    LOCATION = (By.CSS_SELECTOR, "#inputLocation")
    LANGUAGE = (By.CSS_SELECTOR, "#language")
    FREQUENCY = (By.CSS_SELECTOR,"#frequency")
    Google_Analytics = (By.CSS_SELECTOR, "#gaSetupProjectCreate > a")
    SAVE_PROJECT = (By.CSS_SELECTOR,"#step8")
    ICON_BUMBLEBEE = (By.XPATH, '//*[@id="8"]')
    BUTTON_CANCEL_COUNTRY = (By.CSS_SELECTOR, "#clearLocation")
    UPDATE_PROJECT = (By.CSS_SELECTOR, "#ga-step3")
    EDIT_NAME_PROJECT = (By.CSS_SELECTOR, "#name")
    EDIT_LANGUAGE = (By.CSS_SELECTOR, "#language_name")
    CLICK_COUNTRY = (By.CSS_SELECTOR, "#inputLocationautocomplete-list > div")
    CHOOSE_ENGINE = (By.CSS_SELECTOR, "#searchEngine")


class DASHBOARD_PROJECT_LEVELLocators:
    NAME_PROJECT = (By.XPATH,'//span[contains(text(),"Project by Autotest")]')
    Position_Serpwatch = (By.XPATH, '//div[contains(text(),"1")]')
    Search_Volume = (By.CSS_SELECTOR, " div:nth-child(6) > div:nth-child(2) > span")
    Engine = (By.CSS_SELECTOR, "span.pr-t2")
    DELETE_BUTTON = (By.CSS_SELECTOR,"a>.icon-serp-trash.ic-1x5")
    FILTER_BY_NAME = (By.CSS_SELECTOR, "#nameFilter")
    SUCCESS_MESSAGE_ABOUT_DELETE_Project = (By.XPATH, '//span[contains(text(),"Project(s) deleted successfully.")]')
    WINDOW_DELETE = (By.XPATH, '//button[contains(text(),"Delete Project")]')
    Add_Keyword = (By.CSS_SELECTOR, '.table-header > .btn.btn-add-keyword')
    Enter_to_project = (By.XPATH, '//a[contains(text(),"Project")]')
    Input_add_keyword = (By.CSS_SELECTOR, "#keywords_name")
    Button_save_keyword = (By.CSS_SELECTOR, "#save_keywords")
    Position_Serpwatch_for_invalid_keyword = (By.XPATH, '//div[contains(text(),"100+ ")]')
    SUCCESS_MESSAGE_ABOUT_ADD_Keywords = (By.XPATH, '//span[contains(text(),"Keyword(s) added.")]')
    UNSUCCESS_MESSAGE_FOR_lONG_KEYWORD = (By.XPATH, '//span[contains(text(),"Keyword(s) that you have entered have more than 50 characters.")]')
    SELECT_ALL = (By.CSS_SELECTOR, "button.btn.btn-link.btn-select-all")
    BUTTON_DELETE_SELECT_PROJECT = (By.CSS_SELECTOR, 'button.btn.btn-link.btn-delete-all.text-right > i')
    ACCEPT_DELETE = (By.XPATH, '//button[contains(text(),"Delete Projects")]')
    BUTTON_EDIT_Project = (By.CSS_SELECTOR, "i.icon-serp-pencil.ic-1x5")
    FLAG_UKRAINE = (By.XPATH, "//*[contains(@title, 'UA')]")
    LANGUAGE_UKRANIAN = (By.XPATH,"//span[contains(text(), 'Ukrainian')]")
    HOURLY_UPDATE = (By.XPATH, "//span[contains(text(), 'Updated daily')]")
    ENGINE_BING = (By.XPATH, "//span[contains(text(), 'bing.com')]")
    ENTER_IN_FIRST_KEYWORD= (By.CSS_SELECTOR, ".table-small.clickable")

class KEYWORD_Level_Locators:
    SCREENSHOT = (By.CSS_SELECTOR, "a[onclick*= 'api']")
    CLICK_CHART = (By.CSS_SELECTOR, ".amcharts-Circle")
    MODAL_ICON_SCREENSHOT = (By.CSS_SELECTOR)

class NEW_ONBOARDING_Locators:
    Profession = (By.CSS_SELECTOR, "#profession")
    Company = (By.CSS_SELECTOR,"#company")
    Employee = (By.CSS_SELECTOR,"#employee_range")
    Interview_NOTIFICATION = (By.CSS_SELECTOR, ".btn-outline-danger.custom-outline-gray.rounded.mr-3.text-uppercase.px-3")
    Interview_Frequency = (By.CSS_SELECTOR, " div:nth-child(5) > label.btn.btn-outline-warning.rounded.mr-3.text-uppercase.px-3")
    Interview_Competitors = (By.CSS_SELECTOR," div:nth-child(7) > label.btn.btn-outline-success.rounded.mr-3.text-uppercase.px-3")
    Button_Go_App = (By.CSS_SELECTOR,"#btn-submit-survey")

class Billinglocators:
    Name_page = (By.XPATH, '//h1[contains(text(),"Billing")]')

class CLIENT_MANAGMENT_Locators:
    EnableWL = (By.CSS_SELECTOR,"#enabled")
    INPUT_NAME = (By.CSS_SELECTOR,"#name")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "#address")


class ADMINLocators:
    Logout_from_admin =(By.XPATH, '//span[contains(text(),"Logout")]')


