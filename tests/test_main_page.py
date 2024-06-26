from conftest import driver
from locators import Locators


class TestStellarBurgersMainPage:

    # 13) Откроется раздел «Булки» при клике на заголовок "Булки"
    def test_main_rolls_section_opens_from_main_page_click_on_title_rolls_true(self, driver):
        driver.find_element(*Locators.FILLING_BUTTON_MAIN_SCREEN).click()
        driver.find_element(*Locators.ROLLS_BUTTON_MAIN_SCREEN).click()
        title = driver.find_element(*Locators.ROLLS_SECTION_MAIN_SCREEN).get_attribute('class')
        assert 'current' in title

    # 14) Откроется раздел «Соусы» при клике на заголовок "Соусы"
    def test_main_souces_section_opens_from_main_page_click_on_title_souces_true(self, driver):
        driver.find_element(*Locators.FILLING_BUTTON_MAIN_SCREEN).click()
        driver.find_element(*Locators.SAUCES_BUTTON_MAIN_SCREEN).click()
        title = driver.find_element(*Locators.SAUCES_SECTION_MAIN_SCREEN).get_attribute('class')
        assert 'current' in title

    # 15) Откроется раздел «Начинки» при клике на заголовок "Начинки"
    def test_main_filling_section_opens_from_main_page_click_on_title_filling_true(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON_MAIN_SCREEN).click()
        driver.find_element(*Locators.FILLING_BUTTON_MAIN_SCREEN).click()
        title = driver.find_element(*Locators.FILLING_SECTION_MAIN_SCREEN).get_attribute('class')
        assert 'current' in title
