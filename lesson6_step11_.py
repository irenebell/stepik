import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome(ChromeDriverManager().install())
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

try:
    browser.get("http://suninjuly.github.io/registration2.html")
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//form/div[1]/div[1]/input")
    input1.send_keys("Anna")
    input2 = browser.find_element(By.XPATH, "//form/div[1]/div[2]/input")
    input2.send_keys("Petrova")
    input3 = browser.find_element(By.XPATH, "//form/div[1]/div[3]/input")
    input3.send_keys("Email")
    input4 = browser.find_element(By.XPATH, "//form/div[2]/div[1]/input")
    input4.send_keys("Phone")
    input4 = browser.find_element(By.XPATH, "//form/div[2]/div[2]/input")
    input4.send_keys("Adress")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()