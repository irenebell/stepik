import time
import os

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome(ChromeDriverManager().install())
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

try:
    browser.get("http://suninjuly.github.io/file_input.html")
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Anna")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrova")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'new.txt')
    element = browser.find_element(By.NAME, "file") # добавляем к этому пути имя файла
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()