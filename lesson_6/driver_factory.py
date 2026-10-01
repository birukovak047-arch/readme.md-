from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options


def create_driver(brouser = "chrome", headless = False):
    if brouser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Chrome(options=options)
    elif brouser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)
    elif brouser == "safari":
        if headless:
            raise ValueError(f"Опция не поддерживается")
        return webdriver.Safari()
    elif brouser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Edge(options=options)
    else:
        raise ValueError(f"Браузер {brouser} не поддерживается")
