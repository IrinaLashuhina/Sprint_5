import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import login


class TestConstructor:

    def test_navigate_to_buns_section(self, driver):
        #проверка перехода в раздел булки
        login(driver)

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        scroll_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.SCROLL_ELEMENT))
        driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

        driver.find_element(*Locators.BUNS_SECTION).click()
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_SECTION))

        assert active_tab.is_displayed(), "Вкладка 'Булки' не стала активной"

    def test_navigate_to_sauces_section(self, driver):
        #gроверка перехода в раздел cоусы
        login(driver)

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*Locators.SAUCES_SECTION).click()

        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION))
        assert active_tab.is_displayed(), "Вкладка 'Соусы' не стала активной"

    def test_navigate_to_fillings_section(self, driver):
        #переход в раздел начинки
        login(driver)

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*Locators.FILLINGS_SECTION).click()

        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_SECTION))
        assert active_tab.is_displayed(), "Вкладка 'Начинки' не стала активной"