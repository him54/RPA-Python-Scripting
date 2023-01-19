import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://quotes.toscrape.com/')

driver.find_element(By.CSS_SELECTOR,'div.header-box p a').click()
time.sleep(3)
username=driver.find_element(By.CSS_SELECTOR,'input#username')
username.send_keys('abc')
time.sleep(3)
password = driver.find_element(By.CSS_SELECTOR,'input#password')
password.send_keys('abc')
time.sleep(3)
