from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from constants import Constants
from locators import Locators


class TestStellarBurgersLoginPage:

    # 5) Можно залогинеться, по кнопке «Войти в аккаунт» на главной странице
    def test_login_login_to_account_button_from_main_page_valid_email_and_password_true(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.HEADER_ENTER_LOGIN_SCREEN))
        driver.find_element(*Locators.EMAIL_LOGIN_SCREEN).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_LOGIN_SCREEN).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON_LOGIN_SCREEN).click()
        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON)).text
        assert button == 'Оформить заказ'

    # 6) Можно залогинеться, по кнопке «Личный кабинет» на главной странице
    def test_login_personal_account_button_from_main_page_valid_email_and_password_true(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.HEADER_ENTER_LOGIN_SCREEN))
        driver.find_element(*Locators.EMAIL_LOGIN_SCREEN).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_LOGIN_SCREEN).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON_LOGIN_SCREEN).click()
        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON)).text
        assert button == 'Оформить заказ'

    # 7) Можно залогинеться, по кнопке «Войти» в форме регистрации
    def test_login_login_button_from_registration_page_valid_email_and_password_true(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        driver.find_element(*Locators.REGISTER_BUTTON_LOGIN_SCREEN).click()
        driver.find_element(*Locators.ENTER_BUTTON_REGISTER_SCREEN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HEADER_ENTER_LOGIN_SCREEN))
        driver.find_element(*Locators.EMAIL_LOGIN_SCREEN).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_LOGIN_SCREEN).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON_LOGIN_SCREEN).click()
        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON)).text
        assert button == 'Оформить заказ'

    # 8) Можно залогинеться, по кнопке «Войти» в форме восстановления пароля
    def test_login_login_button_from_password_recovery_page_valid_email_and_password_true(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        driver.find_element(*Locators.PASSWORD_RECOVERY_BUTTON_LOGIN_SCREEN).click()
        driver.find_element(*Locators.ENTER_BUTTON_PASSWORD_RECOVERY_SCREEN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HEADER_ENTER_LOGIN_SCREEN))
        driver.find_element(*Locators.EMAIL_LOGIN_SCREEN).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_LOGIN_SCREEN).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON_LOGIN_SCREEN).click()
        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON)).text
        assert button == 'Оформить заказ'
