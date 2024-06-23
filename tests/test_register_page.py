from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators import Locators


faker = Faker()

class TestStellarBurgersRegistrationPage:

    # 1) Успешная регистрация если в поле "Имя" 1 символ и валидные значения полей "Email" и "Пароль"
    def test_registration_name_is_q_and_valid_email_password_login_page(self, driver):
        name = 'Q'
        email = faker.email()
        password = '123456'
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        driver.find_element(*Locators.REGISTER_BUTTON_LOGIN_SCREEN).click()
        driver.find_element(*Locators.NAME_REGISTER_SCREEN).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTER_SCREEN).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REGISTER_SCREEN).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON_REGISTER_SCREEN).click()
        header = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HEADER_ENTER_LOGIN_SCREEN)).text
        assert header == 'Вход'

    # 2) Успешная регистрация если в поле "Email" введён email в формате логин@домен и валидные значения полей "Имя" и "Пароль"
    def test_registration_email_in_format_and_valid_name_login_page(self, driver):
        name = faker.name()
        email = faker.email()
        password = '123456'
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        driver.find_element(*Locators.REGISTER_BUTTON_LOGIN_SCREEN).click()
        driver.find_element(*Locators.NAME_REGISTER_SCREEN).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTER_SCREEN).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REGISTER_SCREEN).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON_REGISTER_SCREEN).click()
        header = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HEADER_ENTER_LOGIN_SCREEN)).text
        assert header == 'Вход'

    # 3) Успешная регистрация если в поле "Пароль" 7 символов и валидные значения полей "Имя" и "Email"
    def test_registration_password_seven_characters_and_valid_name_email_login_page(self, driver):
        name = faker.name()
        email = faker.email()
        password = '1234567'
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        driver.find_element(*Locators.REGISTER_BUTTON_LOGIN_SCREEN).click()
        driver.find_element(*Locators.NAME_REGISTER_SCREEN).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTER_SCREEN).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REGISTER_SCREEN).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON_REGISTER_SCREEN).click()
        header = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HEADER_ENTER_LOGIN_SCREEN)).text
        assert header == 'Вход'

    # 4) При регистрации с паролем из 5 символов появится сообщение об ошибке - "Некорректный пароль"
    def test_registration_password_five_characters_and_valid_name_email_shows_error(self, driver):
        name = faker.name()
        email = faker.email()
        password = '12345'
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_SCREEN).click()
        driver.find_element(*Locators.REGISTER_BUTTON_LOGIN_SCREEN).click()
        driver.find_element(*Locators.NAME_REGISTER_SCREEN).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTER_SCREEN).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REGISTER_SCREEN).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON_REGISTER_SCREEN).click()
        error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR_MESSAGE_REGISTER_SCREEN)).text
        assert error_message == 'Некорректный пароль'
