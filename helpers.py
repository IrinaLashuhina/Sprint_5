from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials
from curl import Urls

def login(driver):
    #авторизация
    driver.get(Urls.MAIN_PAGE)
    driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Credentials.EMAIL)
    driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Credentials.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #ожидание
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))