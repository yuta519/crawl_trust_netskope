from chrome import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def main():
    driver: WebDriver = chrome.initialize_driver(is_headless=True)
    chrome.get(driver, "https://trust.netskope.com/")
    incidents: list[WebElement] = driver.find_elements(
        By.CLASS_NAME, "incident-title")
    a_tags: list = []
    for incident in incidents:
        a_tags += incident.find_elements(By.TAG_NAME, "a")
    for a_tag in a_tags:
        print(a_tag.get_attribute("href"))
    chrome.destroy_driver(driver)


if __name__ == "__main__":
    main()
