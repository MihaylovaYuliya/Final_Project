from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
        alert = browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
browser = webdriver.Chrome()

browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
add_to_basket = browser.find_elment(By.CSS_SELECTOR, ".btn-add-to-basket")
add_to_basket.click()
time.sleep(3)
browser(quit)


