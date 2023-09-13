from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CLASS_NAME, "first")
    input1.send_keys("Archi")
    input2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
    input2.send_keys("Filippov")
    input2 = browser.find_element(By.CLASS_NAME, "third")
    input2.send_keys("archigoodvin08@gmail.com")
    input4 = browser.find_element("xpath", "/html/body/div/form/div[2]/div[1]/input")
    input4.send_keys("+48790241777")
    input5 = browser.find_element("xpath", "/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Poland, Warsaw")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
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