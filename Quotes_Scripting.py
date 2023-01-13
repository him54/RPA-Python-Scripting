import requests
r = requests.get("https://quotes.toscrape.com/")
z = (r.text)
for line in z.split("\n"):
  if '<span class="text" itemprop="text">'in line:
    line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', "") // replace span folder and " 
   line = line.strip() //remove white space
    print(line)

    
    #OUTPUT
    
