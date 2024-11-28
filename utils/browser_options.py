
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_chrome_options():
    options = ChromeOptions()
    options.add_argument("--disable-extensions")
    # todo : If you don't want the incognito mode, just remove it 
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return options

def get_firefox_options():
    options = FirefoxOptions()
    # todo : If you don't want the incognito mode, just remove it 
    options.add_argument("--private")
    return options
