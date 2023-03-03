#source - Banglore    Destination - Delhi  #  https://www.cleartrip.com/

#https://www.cleartrip.com/flights/results?adults=1&childs=0&infants=0&class=Economy&depart_date=23/02/2023&from=BLR&to=DEL&intl=n&origin=BLR%20-%20Bangalore,%20IN&destination=DEL%20-%20New%20Delhi,%20IN&sft=&sd=1677135106809&rnd_one=O&sourceCountry=Bangalore&destinationCountry=New%20Delhi

# /html/body/div[1]/div/main/div/div/div[2]/div[2]/div[8]/div/div[1]/div[1]/div/div[2]/div[3]
# //*[@id="root"]/div/main/div/div/div[2]/div[2]/div[8]/div/div[2]/div[1]/div/div[2]/div[3]/div[2]
#STEPS
#import libraries : using sum necessary libraries selenium , pandas and date time module
#open the browser :  we are using web driver package
#We enter the data into csv we need to use list dictionay and pandas
#Enter the source option  to fill the souce is Banglore and destination is 

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
    
    #OUTPUT - CSV FILE
    ,Name,no,Price
0,IndiGo,6E-687,"7,141"
1,IndiGo,6E-6621,"7,339"
2,IndiGo,6E-2174,"7,339"
3,IndiGo,6E-735,"7,339"
4,IndiGo,6E-2402,"7,339"
5,Air India,AI-501,"7,443"
6,Air India,AI-503,"7,443"
7,Air India,AI-511,"7,443"
8,Air India,AI-808,"7,443"
9,Air India,AI-564,"7,537"
10,SpiceJet,SG-535,"7,578"
11,IndiGo,6E-6813,"7,650"
12,Air Asia,I5-749,"7,700"
13,IndiGo,6E-6465,"7,884"
14,IndiGo,6E-855,"7,912"
15,IndiGo,6E-638,"7,929"
16,IndiGo,6E-2053,"8,179"
17,IndiGo,6E-5039,"8,179"
18,Air Asia,I5-1532,"8,493"
19,Air India,AI-509,"8,493"
20,IndiGo,6E-7382,"8,746"

    
    
    
