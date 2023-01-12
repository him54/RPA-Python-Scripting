import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.imdb.com/chart/top/")
html = r.text
soup = BeautifulSoup(html, 'html.parser')
t = soup.tbody
print(t.attrs) // attributes
tb = soup.find('tbody', {'class':'lister-list'})
t2 = tb.findAll('tr')
for t1 in t2:
  movie_name = t1.find('td', {'class':'titleColumn'})
  print(movie_name.a.string, movie_name.span.string)
