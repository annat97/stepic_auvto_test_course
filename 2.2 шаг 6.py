from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))
link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser. get(link)
try:
    x = browser.find_element(By.ID, "input_value").text
    y= calc(x)
    browser.execute_script("window.scrollBy(0, 200);")
    browser.find_element(By.ID, "answer"). send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(30)
    browser.quit()

