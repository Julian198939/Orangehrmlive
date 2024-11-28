import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver

from utils.browser_options import get_chrome_options, get_firefox_options


@pytest.fixture(scope="function")
def get_driver(request):
    """Pytest fixture to initialize and close the WebDriver."""
    browser = request.config.getoption("--browser")
    if browser.lower() == "chrome":
        options = get_chrome_options()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser.lower() == "firefox":
        options = get_firefox_options()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install(), log_output=None), options=options)
    elif browser.lower() == "safari":
        driver = SafariDriver()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    """Add custom command-line option for browser selection."""
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Specify the browser to use: chrome, firefox, or safari."
    )