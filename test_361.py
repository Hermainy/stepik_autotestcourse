import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.mark.smoke 
def test_login(browser):
    link="https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    signin=browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login ")
    signin.click()
    emailsign=browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    emailsign.send_keys("andreiermilov@bk.ru")
    passwordsign=browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    passwordsign.send_keys("1q2w3e4r5t")
    button=browser.find_element(By.CSS_SELECTOR, "#login_form button")
    button.click()
    assert True

@pytest.mark.parametrize('link_numbers', ['236895', '236896', '236897','236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, link_numbers):
    link = f"https://stepik.org/lesson/{link_numbers}/step/1"
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(str(math.log(int(time.time()))))
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    ).click()
    check=WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    ).text
    assert 'Correct!' == check
    

    