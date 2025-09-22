from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import Urls
from helpers import login

class TestLogin:

    def test_login_from_personal_account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        login(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE

    def test_login_from_main_page_button(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        login(driver)
        order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_registration_form(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        login(driver)
        order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_password_recovery_form(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD).click()
        driver.find_element(*Locators.LOGIN_REGISTRATION).click()
        login(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE