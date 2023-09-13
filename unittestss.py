from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestSuite(unittest.TestCase):
    def test_firsturl(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        
        first_nameInput = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_nameInput.send_keys("Ivan")
        last_nameInput = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_nameInput.send_keys("Ivanych")
        emailInput = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        emailInput.send_keys("seniorQA@mail.ru")
        phoneInput = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
        phoneInput.send_keys("88005553535")
        AddressInput = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
        AddressInput.send_keys("Kukuevo,2lk1")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    def test_secondurl(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        
        first_nameInput = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_nameInput.send_keys("Ivan")
        last_nameInput = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_nameInput.send_keys("Ivanych")
        emailInput = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        emailInput.send_keys("seniorQA@mail.ru")
        phoneInput = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
        phoneInput.send_keys("88005553535")
        AddressInput = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
        AddressInput.send_keys("Kukuevo,2lk1")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()

