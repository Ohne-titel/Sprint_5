from selenium.webdriver.common.by import By


class BurgerLocators:
    LOG_IN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[.='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    REGISTRATION_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # ссылка "Зарегистрироваться"
    NAME_FIELD = (By.XPATH, ".//label[text() = 'Имя']/../input")  # строка для ввода имени
    EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/../input")  # строка для ввода Email
    PASSWORD_FIELD = (By.XPATH, ".//label[text() = 'Пароль']/../input")  # строка для ввода пароля
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(.,'Зарегистрироваться')]")  # кнопка "Зарегистрироваться"
    LOG_IN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")  # кнопка "Войти"
    PLACE_ORDER = (By.XPATH, "//button[contains(.,'Оформить')]")  # кнопка "Оформить заказ"
    PERSONAL_ACCOUNT = (By.XPATH, "//a[.='Личный Кабинет']")  # кнопка "Личный кабинет"
    FORM_FIELDS = (By.XPATH, "//*[@class='Auth_login__3hAey']")  # контейнер ввода данных
    RESET_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # ссылка на "Восстановить пароль"
    LOG_IN_LINK = (By.XPATH, "//a[text()='Войти']")  # ссылка на "Войти" из формы восстановления пароля
    DISPLAYED_ELEMENT = (By.XPATH, "//h1[text()='Соберите бургер']")  # элемент "Соберите бургер" на главной
    PROFILE_ELEMENT = (By.XPATH, "//a[contains(.,'Профиль')]")  # кнопка "Профиль"
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.='Конструктор']")  # кнопка "Конструктор"
    MAKE_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # лого "Stellar Burgers"
    CONTAINER = (By.XPATH, "//*[@class='App_componentContainer__2JC2W']")
    EXIT_BUTTON = (By.XPATH, "//button[contains(.,'Выход')]")  # кнопка "Выход"
    SECTION_BUN = (By.XPATH, ".//span[contains(text(),'Булки')]")  # Список "Булки"
    SECTION_SAUCE = (By.XPATH, ".//span[contains(text(),'Соусы')]")  # Список Соусы"
    ACTIVE_TUB = (By.XPATH, ".//div[contains(@class, 'current')]/span")  # Активная вкладка конструктора
    SECTION_FILLINGS = (By.XPATH, ".//span[contains(text(),'Начинки')]")  # Список "Начинки"



