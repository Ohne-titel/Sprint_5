from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgerLocators
from data import test_login_data


class TestLoginBurger:
    def test_login_main_page_positive(self, driver):
        driver.find_element(*BurgerLocators.LOG_IN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.FORM_FIELDS))

        email_data, password_data = test_login_data()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgerLocators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.PLACE_ORDER))
        assert driver.find_element(*BurgerLocators.DISPLAYED_ELEMENT).is_displayed(), "Title doesn't exist"

    def test_log_in_personal_account_positive(self, driver):
        driver.find_element(*BurgerLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.FORM_FIELDS))

        email_data, password_data = test_login_data()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgerLocators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.PLACE_ORDER))
        assert driver.find_element(*BurgerLocators.DISPLAYED_ELEMENT).is_displayed(), "Title doesn't exist"

    def test_log_in_from_registration_form_positive(self, driver):
        driver.get(f'{URL}login')
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.FORM_FIELDS))

        email_data, password_data = test_login_data()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgerLocators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.PLACE_ORDER))
        assert driver.find_element(*BurgerLocators.DISPLAYED_ELEMENT).is_displayed(), "Title doesn't exist"

    def test_log_in_by_reset_password_positive(self, driver):
        driver.find_element(*BurgerLocators.LOG_IN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.FORM_FIELDS))
        driver.find_element(*BurgerLocators.RESET_PASSWORD_LINK).click()
        driver.find_element(*BurgerLocators.LOG_IN_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.FORM_FIELDS))
        email_data, password_data = test_login_data()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgerLocators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.PLACE_ORDER))
        assert driver.find_element(*BurgerLocators.DISPLAYED_ELEMENT).is_displayed(), "Title doesn't exist"
