import requests
r = requests.get("https://quotes.toscrape.com/")
z = (r.text)
for line in z.split("\n"):
  if '<span class="text" itemprop="text">'in line:
    line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', "") // replace span folder and " 
   line = line.strip() //remove white space
    print(line)

    
    #OUTPUT
    
The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.
It is our choices, Harry, that show what we truly are, far more than our abilities.
There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.
The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.
Imperfection is beauty, madness is genius and it&#39;s better to be absolutely ridiculous than absolutely boring.
Try not to become a man of success. Rather become a man of value.
It is better to be hated for what you are than to be loved for what you are not.
I have not failed. I&#39;ve just found 10,000 ways that won&#39;t work.
A woman is like a tea bag; you never know how strong it is until it&#39;s in hot water.
A day without sunshine is like, you know, night.
