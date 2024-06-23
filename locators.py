from selenium.webdriver.common.by import By


class Locators:
        # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_TO_ACCOUNT_BUTTON_MAIN_SCREEN = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
        # Кнопка "Зарегистрироваться" на странице login
    REGISTER_BUTTON_LOGIN_SCREEN = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/register"]')
        # Поле "Имя" на странице регистрации
    NAME_REGISTER_SCREEN = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"][1]//input[@name="name"]')
        # Поле "Email" на странице регистрации
    EMAIL_REGISTER_SCREEN = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"][2]//input[@name="name"]')
        # Поле "Пароль" на странице регистрации
    PASSWORD_REGISTER_SCREEN = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"]//input[@type="password"]')
        # Кнопка "Зарегистрироваться" на странице регистрации
    REGISTER_BUTTON_REGISTER_SCREEN = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
        # Заголовок "Вход" на странице login
    HEADER_ENTER_LOGIN_SCREEN = (By.XPATH, '//h2[text()="Вход"]')
        # Сообщение об ошибке на странице регистрации
    PASSWORD_ERROR_MESSAGE_REGISTER_SCREEN = (By.XPATH, '//p[@class="input__error text_type_main-default"]')
        # Кнопка "Личный кабинет на главной странице
    PERSONAL_ACCOUNT_BUTTON_MAIN_SCREEN = (By.XPATH, '//a[@href="/account"]/p[@class="AppHeader_header__linkText__3q_va ml-2"]')
        # Поле "Email" на странице login
    EMAIL_LOGIN_SCREEN = (By.XPATH, '//input[@name="name"]')
        # Поле "Пароль" на странице login
    PASSWORD_LOGIN_SCREEN = (By.XPATH, '//input[@type="password"]')
        # Кнопка "Войти" на странице login
    ENTER_BUTTON_LOGIN_SCREEN = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
        # Кнопка "Оформить заказ" на главной странице
    PLACE_AN_ORDER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
        # Кнопка "Войти" на странице регистрации
    ENTER_BUTTON_REGISTER_SCREEN = (By.XPATH, '//p/a[@class="Auth_link__1fOlj"]')
        # Кнопка "Восстановить пароль" на странице login
    PASSWORD_RECOVERY_BUTTON_LOGIN_SCREEN = (By.XPATH, '//a[@href="/forgot-password"]')
        # Кнопка "Войти" на странице восстановления пароля
    ENTER_BUTTON_PASSWORD_RECOVERY_SCREEN = (By.XPATH, '//p/a[@class="Auth_link__1fOlj"]')
        # Текст описания раздела
    TEXT_OF_PAGE_DESCRIPTION = (By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]')
        # Кнопка "Выход" на странице личного кабинета
    EXIT_BUTTON_PERSONAL_ACCOUNT_SCREEN = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
        # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON_PERSONAL_ACCOUNT_SCREEN = (By.XPATH, '//a[@href="/"]/p[@class="AppHeader_header__linkText__3q_va ml-2"]')
        # Заголовок "Соберите бургер" на странице конструктора
    HEADER_CONSTRUCT_BURGER_CONSTRUCTOR_PAGE = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')
        # Логотип Stellar Burgers
    LOGO_STELLAR_BURGERS_PERSONAL_ACCOUNT_SCREEN = (By.XPATH, '//div/a[@href="/"]')
