from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgerLocators


class TestExitAccount:
    def test_exit_account(self, driver):
        driver.find_element(*BurgerLocators.LOG_IN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys("miagkova.elina@mail.ru")
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*BurgerLocators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.PLACE_ORDER))
        driver.find_element(*BurgerLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(URL + 'account/profile'))
        driver.find_element(*BurgerLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(URL + 'login'))
        assert driver.find_element(*BurgerLocators.FORM_FIELDS).is_displayed()
