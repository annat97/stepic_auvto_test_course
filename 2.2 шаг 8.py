from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser= webdriver.Chrome()
browser.get("https://suninjuly.github.io/file_input.html")

try:
    browser.find_element(By.NAME, "firstname").send_keys("ivan")
    browser.find_element(By.NAME, "lastname").send_keys("petrov")
    browser.find_element(By.NAME, "email").send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "загрузка.txt")

    browser.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(30)
    browser.quit()

