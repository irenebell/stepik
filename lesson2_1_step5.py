import time
from math import *

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def calc(x):
   return str(log(abs(12 * sin(int(x)))))

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome(ChromeDriverManager().install())
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

try:
    browser.get("http://suninjuly.github.io/math.html")
    # находим х

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)


    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

# отмечаем чекбокс
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

# отмечаем радиобаттон
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()