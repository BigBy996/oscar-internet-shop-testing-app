import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from const_storage import TestConfig


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Choose language')


@pytest.fixture()
def browser(request):
    TestConfig.browser = request.config.getoption("browser_name")
    TestConfig.language = request.config.getoption("language")
    if TestConfig.browser == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': TestConfig.language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif TestConfig.browser == "firefox":
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", TestConfig.language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(TestConfig.browser))
        browser = None
    yield browser
    print("\nquit browser...")
    browser.quit()
