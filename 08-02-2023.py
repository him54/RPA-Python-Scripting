from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from _datetime import datetime
import os
import sys
application_path = os.path.dirname(sys.executable) #if we fine our director
now = datetime.now()
dt=now.strftime("%m%d%y")
print(dt)
option = Options()
option.headless = True

driver_service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=driver_service, options=option)
driver.get('https://www.thesun.co.uk/sport/football/')

title_list=[]
subtitle_list=[]
link_list=[]
#<div class="teaser__copy-container"><a class="text-anchor-wrap" href="https://www.thesun.co.uk/sport/21296749/chelsea-hire-mental-coach-blacks-winning-culture/"><h3 class="teaser__headline t-p-color">IN-OKA</h3><p class="teaser__subdeck"> Chelsea hire All Blacks' mental skills coach to help create winning culture</p></a></div>
#*[@id="customiser-v2-13503409"]/div[9]/div/div[3]/div/div[2]

containers = driver.find_elements(By.XPATH, value= '//div[@class="teaser__copy-container"]')
for container in containers:
    title = container.find_element(By.XPATH, value='./a/h3').text
    subtitle = container.find_element(By.XPATH, value='./a/p').text
    link = container.find_element(By.XPATH,value='./a').get_attribute('href')
    title_list.append(title)
    subtitle_list.append(subtitle)
    link_list.append(link)

d={'Title':title_list,'Subtitle':subtitle_list, 'Link': link_list}
dataframe = pd.DataFrame(d)
filename = f'news_{dt}.csv'
#final_path=os.path.join(application_path, filename)
dataframe.to_csv(filename)
driver.quit()
