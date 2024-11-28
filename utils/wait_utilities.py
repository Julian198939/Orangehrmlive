from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element_visible(driver, locator, timeout=10):
    """Wait for an element to be visible."""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_for_element_clickable(driver, locator, timeout=10):
    """Wait for an element to be clickable."""
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def wait_for_url_to_be(driver, url, timeout=10):
    """Wait for the URL to be a specific value."""
    return WebDriverWait(driver, timeout).until(EC.url_to_be(url))