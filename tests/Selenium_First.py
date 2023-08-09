import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver


def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)
    assert "Login - VWO" in driver.title
