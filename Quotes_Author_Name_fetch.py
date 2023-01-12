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
print(t.attrs) #output - {'class': ['text'], 'itemprop': 'text'}  (Dictionary Form)

#output
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“It is our choices, Harry, that show what we truly are, far more than our abilities.”
“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
“Try not to become a man of success. Rather become a man of value.”
“It is better to be hated for what you are than to be loved for what you are not.”
“I have not failed. I've just found 10,000 ways that won't work.”
“A woman is like a tea bag; you never know how strong it is until it's in hot water.”
“A day without sunshine is like, you know, night.”
Albert Einstein
J.K. Rowling
Albert Einstein
Jane Austen
Marilyn Monroe
Albert Einstein
André Gide
Thomas A. Edison
Eleanor Roosevelt
Steve Martin
