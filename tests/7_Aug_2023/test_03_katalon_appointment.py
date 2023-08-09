import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.negative
def test_katalon_appointment_Negative():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(3)

    driver.find_element(By.ID, "btn-make-appointment").click()
    time.sleep(3)

    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    time.sleep(3)

    driver.find_element(By.ID, "txt-password").send_keys("John Doe")
    time.sleep(3)

    driver.find_element(By.ID, "btn-login").click()

    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed!" in error_message.text


@pytest.mark.positive
def test_katalon_appointment():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(3)

    driver.find_element(By.ID, "btn-make-appointment").click()
    time.sleep(3)

    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    time.sleep(3)

    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    time.sleep(3)

    driver.find_element(By.ID, "btn-login").click()

    dropdown = Select(driver.find_element(By.ID, "combo_facility"))
    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")
    time.sleep(3)

    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    time.sleep(3)

    driver.find_element(By.ID, "radio_program_medicaid").click()
    time.sleep(3)

    driver.find_element(By.ID, "txt_visit_date").send_keys("12/12/1991")
    time.sleep(3)

    driver.find_element(By.ID, "txt_comment").send_keys("I have fever with 101")
    time.sleep(5)

    driver.find_element(By.ID, "btn-book-appointment").click()
    time.sleep(7)

    heading_h2 = driver.find_element(By.TAG_NAME, "h2")

    assert "Appointment Confirmation" in heading_h2.text
    time.sleep(9)
