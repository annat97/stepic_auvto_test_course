import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser. get(link)
try:
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    result = int(num1) + int(num2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
       time.sleep(30)
       browser.quit()
       