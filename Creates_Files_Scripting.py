import requests
r = requests.get("https://quotes.toscrape.com/")
z = (r.text)
with open('quotes.txt', 'w') as f: // quote written in text file
  for line in z.split("\n"):
    if '<span class="text" itemprop="text">'in line:
      line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', "")   #replace span folder
      line = line.strip()
      f.write(line)
      f.write('\n')
