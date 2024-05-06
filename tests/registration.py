from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import test_registration_data
from locators import BurgerLocators


class TestRegistrationBurger:

    def test_registration_positive(self, driver):
        driver.find_element(*BurgerLocators.LOG_IN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.REGISTRATION_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.FORM_FIELDS))

        email_data = test_registration_data()

        driver.find_element(*BurgerLocators.NAME_FIELD).send_keys("Элина")
        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*BurgerLocators.REGISTRATION_BUTTON).click()

        assert driver.find_element(By.XPATH, "//*[@class='Auth_login__3hAey']").is_displayed()

    def test_registration_invalid_password_negative(self, driver):
        driver.find_element(*BurgerLocators.LOG_IN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.REGISTRATION_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocators.FORM_FIELDS))

        email_data = test_registration_data()

        driver.find_element(*BurgerLocators.NAME_FIELD).send_keys("Элина")
        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys("12345")
        driver.find_element(*BurgerLocators.REGISTRATION_BUTTON).click()

        assert driver.find_element(By.XPATH, "//p[contains(.,'Некорректный пароль')]").is_displayed()
