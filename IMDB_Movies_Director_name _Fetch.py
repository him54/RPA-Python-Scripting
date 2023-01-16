from bs4 import BeautifulSoup
import requests

moviename = input("Enter the movie name")
moviename = moviename.lower()

r=requests.get('https://www.imdb.com/chart/top/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
tb=soup.find('tbody',{'class':'lister-list'})
trs=tb.findAll('tr',{'class'})
trs=tb.findAll('tr')

for tr in trs:
  td= tr.find('td',{'class':'titleColumn'})
  imdbmovie=td.a.string.strip().lower()
  # print(imdbmovie)
  if moviename == imdbmovie:
    movieid = td.a['href']
    # print(movieid)
    movieurl = f'https://www.imdb.com/{movieid}'
    #print(movieurl)
    r1 = requests.get('https://www.imdb.com/{movieid}')
    html = r1.text
    soup2 = BeautifulSoup(html, 'html.parser')
    print(soup2)
    # div = soup.find('div', {'class'} : )
