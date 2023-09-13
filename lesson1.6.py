from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
	
    link = browser.find_element(By.LINK_TEXT, text)
    link.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(first_name)
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys(last_name)
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys(city)
    input4 = browser.find_element_by_id("country")
    input4.send_keys(country)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла