from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgerLocators


class TestSwitchToAccount:
    def test_switch_to_personal_account_positive(self, driver):
        driver.find_element(*BurgerLocators.LOG_IN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys("miagkova.elina@mail.ru")
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*BurgerLocators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.PLACE_ORDER))
        driver.find_element(*BurgerLocators.PERSONAL_ACCOUNT).click()
        assert driver.current_url == f'{URL}account'
        # assert driver.find_element(*BurgerLocators.PROFILE_ELEMENT).is_displayed(), "Element doesn't exist"
        driver.quit()

    def test_switch_to_constructor_positive(self, driver):
        driver.find_element(*BurgerLocators.LOG_IN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys("miagkova.elina@mail.ru")
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*BurgerLocators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.PLACE_ORDER))
        driver.find_element(*BurgerLocators.PERSONAL_ACCOUNT).click()
        driver.find_element(*BurgerLocators.CONSTRUCTOR_LINK).click()
        driver.find_element(*BurgerLocators.MAKE_BURGER).click()
        assert driver.find_element(*BurgerLocators.DISPLAYED_ELEMENT).is_displayed()
        driver.quit()
