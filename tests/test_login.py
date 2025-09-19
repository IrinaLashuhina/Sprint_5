from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import Urls
from data import Credentials


class TestLogin:

    #вход через кнопку Личный кабинет
    def test_login_from_personal_account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()


        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE

    #вход через кнопку Войти в аккаунт на главной странице
    def test_login_from_main_page_button(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    #вход через кнопку Войти на странице регистрации
    def test_login_from_registration_form(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()

        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    #вход через кнопку Войти в форме восстановления пароля
    def test_login_from_password_recovery_form(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD).click()
        driver.find_element(*Locators.LOGIN_REGISTRATION).click()

        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE