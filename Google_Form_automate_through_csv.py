from selenium.webdriver.common.by import By
import csv
from selenium import webdriver
import time

with open('data.csv', 'r') as f:
    z = f.readlines()
    details = z[1].split()
    print(details)
# OPEN GOOGLE FORM IN CHROME
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSelgrZw0-S-Yf7OjFLAmYZ22XzZvuuJu4gkhEUitAcZiQHQKQ/viewform')
time.sleep(3

# NAME IN GOOGLE FORM
name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div['
'1]/input')
name.send_keys(details[0])
time.sleep(3)

# EMAIL IN GOOGLE FORM
email = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div['
'1]/input')
email.send_keys(details[1])
time.sleep(3)

# PHONE NUMBER IN GOOGLE FORM
phone = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div['
'1]/input')
phone.send_keys(details[2])
time.sleep(3)

# SUBMIT IN GOOGLE FORM
driver.find_element(By.CSS_SELECTOR, 'span.NPEfkd.RveJvd.snByac').click()
time.sleep(3)


