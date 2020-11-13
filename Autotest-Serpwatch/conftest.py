import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Choose browser: ru, en,... (etc.)",
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        print("\n\nStart chrome browser for test...")
        # for linux or ubuntu
        # browser = webdriver.Chrome(options=options, executable_path="./chromedriver")
        browser = webdriver.Chrome(options=options)
        browser.delete_all_cookies()
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        print("\n\nStart firefox browser for test...")
        # for linux or ubuntu
        # browser = webdriver.Firefox(firefox_profile=fp, executable_path="./geckodriver")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.delete_all_cookies()
    yield browser
    print("\nquit browser..")
    browser.quit()

