from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/redirect_accept.html")
try:
    first_window = browser.window_handles[0]
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    browser.execute_script("arguments[0].click();", button)
    time.sleep(2)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(20)
    browser.quit()
