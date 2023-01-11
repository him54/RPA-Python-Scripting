import requests
for i in range(1,11):
  url = f'https://quotes.toscrape.com/page/{i}/'
  r = requests.get(url)
  z = r.text
  with open('quotes.txt', 'a',encoding='utf-8') as f: //  apppend value
    for line in z.split("\n"):
      if '<span class="text" itemprop="text">'in line:
        line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', "")
        line = line.strip()
        f.write(line)
        f.write('\n')
