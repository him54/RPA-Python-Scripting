#source - Banglore    Destination - Delhi  #  https://www.cleartrip.com/

#https://www.cleartrip.com/flights/results?adults=1&childs=0&infants=0&class=Economy&depart_date=23/02/2023&from=BLR&to=DEL&intl=n&origin=BLR%20-%20Bangalore,%20IN&destination=DEL%20-%20New%20Delhi,%20IN&sft=&sd=1677135106809&rnd_one=O&sourceCountry=Bangalore&destinationCountry=New%20Delhi

# /html/body/div[1]/div/main/div/div/div[2]/div[2]/div[8]/div/div[1]/div[1]/div/div[2]/div[3]
# //*[@id="root"]/div/main/div/div/div[2]/div[2]/div[8]/div/div[2]/div[1]/div/div[2]/div[3]/div[2]
#STEPS
#import libraries : using sum necessary libraries selenium , pandas and date time module
#open the browser :  we are using web driver package
#We enter the data into csv we need to use list dictionay and pandas
#Enter the source option  to fill the souce is Banglore and destination is delhi

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
# We click search button for searching the flights

from datetime import *
import os
import sys
import pandas as pd
from time import *
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


driver = webdriver.Chrome(executable_path='chromedriver')

driver.get('https://www.cleartrip.com/flights')


From=driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[1]/input')
sleep(3)
From.send_keys("Bangalore")
driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[1]/div[2]/ul[1]/li/div/div[2]/p').click()
To=driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[3]/input')
sleep(3)
To.send_keys("Delhi")
sleep(3)
driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[3]/div[2]/ul/li/div/div[2]/p').click()
sleep(3)
driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[4]/div/div[2]/span').click()
sleep(5)
i=1

SCROLL_PAUSE_TIME = 0.5

last_height = driver.execute_script("return document.body.scrollHeight")


containers=driver.find_elements(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[8]/div/div")
print(len(containers))
FN = []
FNO = []
P = []
for container in containers:
    flightname =  container.find_element(By.XPATH, "./div[1]/div/div[2]/div[1]/div/div/div[3]/p[1]").text
    flightno = container.find_element(By.XPATH, "./div[1]/div/div[2]/div[1]/div/div/div[3]/p[2]").text
    price = container.find_element(By.XPATH, "./div[1]/div/div[2]/div[3]/div[2]/div/p").text
    if 'Seat' in price:
        price=container.find_element(By.XPATH, "./div[1]/div/div[2]/div[3]/div[2]/div/p[2]").text

    print(flightname,flightno,price)
    FN.append(flightname)
    FNO.append(flightno)
    P.append(price)

d={'Name':FN,'no':FNO,'Price':P}
df=pd.DataFrame(d)

df['Price']=df['Price'].str.replace('₹','')

filename='CA1.csv'
df.to_csv(filename)

df = pd.read_csv('CA1.csv')
cheapest_price = df['Price'].iloc[0]
cheapest_flight = df['Name'].iloc[0]

print(f"The cheapest flight price is {cheapest_price} and cheapest flight name is {cheapest_flight}.")


        #/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[8]/div/div[1]/div[1]/div/div[2]/div[3]
        #//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[8]/div/div[2]/div[1]/div/div[2]/div[3]/div[2]
    
    
    
