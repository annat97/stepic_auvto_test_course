from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля — уникальные селекторы по placeholder
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    input1.send_keys("Имя")

    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    input2.send_keys("Фамилия")

    input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    input3.send_keys("Почта")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()