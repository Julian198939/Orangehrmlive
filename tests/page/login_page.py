from selenium.webdriver.common.by import By
from utils.wait_utilities import wait_for_element_visible, wait_for_element_clickable, wait_for_url_to_be

class LoginPage:

  def __init__(self, driver):
    self.driver = driver
    self.username_field = (By.NAME, "username")
    self.password_field = (By.NAME, "password")
    self.login_button = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button")
    self.error_message = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-alert-content-text")
    self.blank_err_message = (By.CSS_SELECTOR, "span.oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message:nth-child(3)")
   
  def wait_for_page_to_load(self, url, timeout=10):
      """Wait for the URL to match a specific value."""
      wait_for_url_to_be(self.driver, url, timeout)

  def enter_text(self, locator, text, timeout=10):
      """Enter text into a field."""
      field = wait_for_element_visible(self.driver, locator, timeout)
      field.clear()
      field.send_keys(text)

  def click_element(self, locator, timeout=10):
      """Click an element."""
      wait_for_element_clickable(self.driver, locator, timeout).click()


  def link_fully_visible(self):
      self.wait_for_page_to_load("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

  def enter_username(self, username):
      self.enter_text(self.username_field, username)

  def enter_password(self, password):
      self.enter_text(self.password_field, password)

  def click_login(self):
      self.click_element(self.login_button)
   
  def login_link_visible(self):
      self.wait_for_page_to_load("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
      

  def get_error_message(self):
      return wait_for_element_visible(self.driver, self.error_message).text
      # Invalid credentials

  def blank_error_message(self):
      return wait_for_element_visible(self.driver, self.blank_err_message).text
      # Required
