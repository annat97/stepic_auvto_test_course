import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера
driver = webdriver.Chrome()

# пауза 5 секунд
time.sleep(5)

# открываем сайт
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

# ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# пишем текст в поле
textarea.send_keys("get()")
time.sleep(5)

# ищем кнопку отправки
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# нажимаем на кнопку
submit_button.click()
time.sleep(5)

# закрываем браузер
driver.quit()