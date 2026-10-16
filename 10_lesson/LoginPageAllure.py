"""
Page Object для страницы авторизации SauceDemo.
URL: https://www.saucedemo.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    """Класс для взаимодействия со страницей авторизации."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver) -> None:
        """
        Инициализация страницы.

        :param driver: экземпляр WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str) -> "LoginPage":
        """
        Открыть страницу авторизации.

        :param url: адрес страницы.
        :type url: str
        :return: экземпляр текущего класса.
        :rtype: LoginPage
        """
        self.driver.get(url)
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """
        Выполнить вход с указанными учётными данными.

        :param username: имя пользователя.
        :type username: str
        :param password: пароль.
        :type password: str
        :return: экземпляр текущего класса.
        :rtype: LoginPage
        """
        self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)
        self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()
        return self

    @allure.step("Нажатие кнопки 'Login'")
    def click_login(self):
        """
        Нажимает кнопку входа.

        :return: None
        """
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
