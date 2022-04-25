import platform

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def _decide_chromedriver_by_os() -> str:
    os = platform.system()
    if os == "Windows":
        return "chrome/win/chromedriver"
    elif os == "Darwin":
        return "chrome/mac/chromedriver"
    elif os == "Linux":
        return "chrome/linux/chromedriver"


_chrome_driver_path = _decide_chromedriver_by_os()


def initialize_driver(is_headless: bool = False) -> WebDriver:
    options = webdriver.ChromeOptions()
    if is_headless:
        options.add_argument("--headless")
    return webdriver.Chrome(executable_path=_chrome_driver_path, options=options)


def get(driver: WebDriver, url: str) -> None:
    driver.get(url)


def fetch_pagesource(driver: WebDriver) -> str:
    return driver.page_source


def fetch_page_title(driver: WebDriver) -> str:
    return driver.title


def destroy_driver(driver: WebDriver) -> None:
    driver.close()
