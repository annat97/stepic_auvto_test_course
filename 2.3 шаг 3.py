from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))   
browser= webdriver.Chrome()
browser.get("https://suninjuly.github.io/alert_accept.html")
try:
    browser.find_element(By.XPATH, "//button[contains(text(),'magical journey')]").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x =browser.find_element(By.ID, "input_value").text
    y =calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()

finally:
   time.sleep(20)
   browser.quit()
   
