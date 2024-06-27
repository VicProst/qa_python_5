from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import login
from conftest import driver
from locators import Locators


class TestStellarBurgersAccountProfilePage:

    # 9) Страница личного кабинета откроется из главной страницы по клику на кнопку "Личный кабинет", если пользователь зарегистрирован
    def test_personal_account_personal_account_page_open_from_from_main_page_user_is_logged_in_true(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TEXT_OF_PAGE_DESCRIPTION)).text
        assert text == 'В этом разделе вы можете изменить свои персональные данные'

    # 10) Выход из аккаунта и переход на страницу входа из страницы личного кабинета по клику на кнопку "Выйти", пользователь выйдет из аккаунта
    def test_personal_account_log_out_and_open_login_page_click_on_exit_button_true(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TEXT_OF_PAGE_DESCRIPTION))
        driver.find_element(*Locators.EXIT_BUTTON_PERSONAL_ACCOUNT_SCREEN).click()
        header = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HEADER_ENTER_LOGIN_SCREEN)).text
        assert header == 'Вход'

    # 11) Страница конструктора откроется из страницы личного кабинета по клику на кнопку "Конструктор"
    def test_personal_account_constructor_page_opens_from_personal_account_page_click_on_constructor_button_true(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TEXT_OF_PAGE_DESCRIPTION))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON_PERSONAL_ACCOUNT_SCREEN).click()
        header = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HEADER_CONSTRUCT_BURGER_CONSTRUCTOR_PAGE)).text
        assert header == 'Соберите бургер'

    # 12) Страница конструктора откроется из страницы личного кабинета по клику на логотип "Stellar Burgers"
    def test_personal_account_constructor_page_opens_from_personal_account_page_click_on_logo_button_true(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TEXT_OF_PAGE_DESCRIPTION))
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS_PERSONAL_ACCOUNT_SCREEN).click()
        header = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HEADER_CONSTRUCT_BURGER_CONSTRUCTOR_PAGE)).text
        assert header == 'Соберите бургер'
