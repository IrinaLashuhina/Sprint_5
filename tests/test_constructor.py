from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials
from curl import Urls


def login(driver):

    driver.get(Urls.MAIN_PAGE)
    driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Credentials.EMAIL)
    driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Credentials.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))


def test_navigate_to_buns_section():

    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        login(driver)

        #переход в конструктор
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        #прокрутка к элементу конструктора
        scroll_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.SCROLL_ELEMENT))
        driver.execute_script("arguments[0].scrollIntoView();", scroll_element)


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUNS_SECTION))
        driver.find_element(*Locators.BUNS_SECTION).click()


        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION))
        assert active_tab.is_displayed(), "Вкладка 'Булки' не стала активной"

    finally:
        driver.quit()


def test_navigate_to_sauces_section():

    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        login(driver)


        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAUCES_SECTION))
        driver.find_element(*Locators.SAUCES_SECTION).click()


        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION))
        assert active_tab.is_displayed(), "Вкладка 'Соусы' не стала активной"

    finally:
        driver.quit()


def test_navigate_to_fillings_section():

    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        login(driver)


        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FILLINGS_SECTION))
        driver.find_element(*Locators.FILLINGS_SECTION).click()


        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION))
        assert active_tab.is_displayed(), "Вкладка 'Начинки' не стала активной"

    finally:
        driver.quit()