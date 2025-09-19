import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import Urls
from geniration_ep import EmailPasswordGenerator

@pytest.mark.usefixtures("driver")
class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        name = "TestUser"
        email = EmailPasswordGenerator.generate_email()
        password = EmailPasswordGenerator.generate_password()

        driver.find_element(*Locators.NAME_REGISTRATION).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE

    def test_invalid_password(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        name = "TestUser"
        email = EmailPasswordGenerator.generate_email()
        password = "12345"
        driver.find_element(*Locators.NAME_REGISTRATION).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PASSWORD_ERROR)        )
        assert error_message.is_displayed() and "Некорректный пароль" in error_message.text