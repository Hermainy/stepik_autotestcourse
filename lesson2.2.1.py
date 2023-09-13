from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.CSS_SELECTOR, "#num1").text
    b = browser.find_element(By.CSS_SELECTOR, "#num2").text
    res=int(a)+int(b)
    result=str(res)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(result)

    button=browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
