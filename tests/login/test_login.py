import pytest
import time


from tests.page.login_page import LoginPage

@pytest.fixture()
def setup(get_driver):
    driver = get_driver
    login_page = LoginPage(driver)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
    yield driver, login_page


def test_valid_login(setup):
    driver, login_page = setup
    login_page = LoginPage(driver)
    
    # wait until link is fully visible
    login_page.link_fully_visible()
    print("URL is fully loaded and visible!")
    
    # Enter valid username & pwd
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    
    # click login btn
    login_page.click_login()
    
    # assert successfully login and then redirect to dashboard
    login_page.login_link_visible()
    time.sleep(5)
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"


def test_invalid_login(setup):
    driver, login_page = setup
    login_page = LoginPage(driver)
  
    # Enter valid username and invalid pwd
    login_page.enter_username("Admin")
    login_page.enter_password("wrong01password")

    # click login btn
    login_page.click_login()

    # assert err msg displayed
    err_msg = login_page.get_error_message()
    assert err_msg == "Invalid credentials"
  
def test_left_inputfield_blank(setup):
    driver, login_page = setup
    login_page = LoginPage(driver)

    # click login btn
    login_page.click_login()

    # assert blank msg displayed
    blank_err_msg = login_page.blank_error_message()
    assert blank_err_msg == "Required"
