import time
from selenium.webdriver.support.ui import Select

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome(ChromeDriverManager().install())
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

try:
    browser.get("http://suninjuly.github.io/selects1.html")

    number1 = browser.find_element(By.ID, "num1")
    number2 = browser.find_element(By.ID, "num2")
    summa = int(number1.text) + int(number2.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summa))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()