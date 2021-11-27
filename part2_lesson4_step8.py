from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    button = browser.find_element_by_css_selector("button[id=book]")
    button.click()



 


    x_element = browser.find_element_by_css_selector('.form-group .nowrap#input_value')
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element_by_css_selector('.form-group #answer  ')
    y_element.send_keys(y)

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()