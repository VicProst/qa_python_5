import pytest
from selenium import webdriver
from constants import Constants
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_SCREEN).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.HEADER_ENTER_LOGIN_SCREEN))
    driver.find_element(*Locators.EMAIL_LOGIN_SCREEN).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD_LOGIN_SCREEN).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.ENTER_BUTTON_LOGIN_SCREEN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
