from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgerLocators


class TestConstructorElements:
    def test_switch_to_sauce(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.SECTION_SAUCE))
        driver.find_element(*BurgerLocators.SECTION_SAUCE).click()
        assert driver.find_element(*BurgerLocators.ACTIVE_TUB).text == 'Соусы'

    def test_switch_section_fillings(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.SECTION_FILLINGS))
        driver.find_element(*BurgerLocators.SECTION_FILLINGS).click()
        assert driver.find_element(*BurgerLocators.ACTIVE_TUB).text == 'Начинки'

    def test_switch_section_bun(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.SECTION_BUN))
        driver.find_element(*BurgerLocators.SECTION_SAUCE).click()
        driver.find_element(*BurgerLocators.SECTION_BUN).click()
        assert driver.find_element(*BurgerLocators.ACTIVE_TUB).text == 'Булки'

