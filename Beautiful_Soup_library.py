#Beautiful soup library - import bs4 
class of bs4
from bs4 import BeautifulSoup
import requests
r = requests.get('https: #quotes.toscrape.com/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(type(html))
print(type(soup))

from bs4 import BeautifulSoup
import requests
r = requests.get('https:  #quotes.toscrape.com/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(type(html))
print(soup.title) # title name

from bs4 import BeautifulSoup
import requests
r = requests.get('https: #quotes.toscrape.com/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(type(html))
print(soup.title.string) # remove tags and print the title of website
