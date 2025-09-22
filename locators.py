from selenium.webdriver.common.by import By


class Locators:
    #главная_страница
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")


    #рег

    NAME_REGISTRATION = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_REGISTRATION = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")

    LOGIN_REGISTRATION = (By.XPATH, "//a[contains(text(), 'Войти')]")

    #страница_login
    EMAIL_LOGIN = (By.XPATH, "//input[@name='name']")
    PASSWORD_LOGIN = (By.XPATH, "//input[@type='password']")

    LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти']"]
    FORGOT_PASSWORD = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

    #лич_кабинет
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    #конструктор
    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]/..")
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]/..")
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]/..")
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    #логотип
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

    SCROLL_ELEMENT = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Соус традиционный галактический']")
    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]/..")
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
