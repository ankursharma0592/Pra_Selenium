import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwologin():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver. get("https://app.vwo.com/#/login")

    link = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    link.click()

    time.sleep(5)
    assert "Get Started with Free Trial | VWO" in driver.title

