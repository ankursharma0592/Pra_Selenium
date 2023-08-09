import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://app.vwo.com/#/login")

    email_address = driver.find_element(By.ID, "login-username")
    email_address.send_keys("ankursharma.0592@yahoo.com")

    password = driver.find_element(By.ID, "login-password")
    password.send_keys("As@9669302381")

    button = driver.find_element(By.ID, "js-login-btn")
    button.click()

    time.sleep(5)
    LOGGER.info('title is ' + driver.title)
    assert "Dashboard" in driver.title
