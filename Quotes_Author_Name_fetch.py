from bs4 import BeautifulSoup
import requests
r = requests.get('https://quotes.toscrape.com/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
t = soup.span
for q in soup.findAll('span', {'class':'text'}): // All data present in a page
  print(q.string)
for a in soup .findAll('small', {'class':'author'}):
  print(a.string)
print(t.attrs) #attributes
