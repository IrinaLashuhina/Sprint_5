from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import Urls
from data import Credentials


class TestAccountNavigation:

    def login(self, driver):
        #авторизация
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_go_to_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE

    def test_go_from_account_to_constructor_by_button(self, driver):
        self.login(driver)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.ACCOUNT_PAGE))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE

    def test_go_from_account_to_constructor_by_logo(self, driver):
        self.login(driver)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.ACCOUNT_PAGE))
        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE

    def test_logout_from_account(self, driver):
        self.login(driver)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.ACCOUNT_PAGE))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE