import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('https://www.deepl.com/en/translator')

driver.find_element(By.CSS_SELECTOR, '.mt-4 button').click()
time.sleep(3)

hi = driver.find_element(By.CSS_SELECTOR, '.lmt__inner_textarea_container textarea')
hi.send_keys('bonjour')
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, 'button.lmt__language_select__active').click()
time.sleep(5)
