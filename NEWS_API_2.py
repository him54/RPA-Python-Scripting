import requests

categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

country = input("Enter the country code: ")

print("Available news categories:")
for i, category in enumerate(categories):
    print(f"{i+1}. {category}")
category_index = int(input("Enter the number: "))
category = categories[category_index-1]

api_key = "7ab367c237e9497897d30c4552524021"
url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"
response = requests.get(url)
data = response.json()
articles = data["articles"]

for i, article in enumerate(articles, start=1):
    print(f"{i}. {article['title']}")
    
    
    
    #OUTPUT
     Enter the country code: in
Available news categories:
1. business
2. entertainment
3. general
4. health
5. science
6. sports
7. technology
Enter the number: 6
1. Impact Player could allow Rajasthan Royals to maximise strong core - ESPNcricinfo
2. Shikhar Dhawan Took HIV Test When He Was "14-15 Years Old" After Manali Trip. This Happened Next - NDTV Sports
3. IPL 2023: Shardul Thakur, Sunil Narine in race for Kolkata Knight Riders captaincy - Indiatimes.com
4. Video: Unimpressed Fan Body Shames Pakistan Cricketer Azam Khan During 2nd T20I vs Afghanistan - NDTV Sports
5. SA vs WI, 2nd T20I: Over 500 Runs Scored, Record-breaking Number of Boundaries - News18
6. Harmanpreet breaks knockout curse and Lanning's challenge to cap off fitting WPL finale - ESPNcricinfo
7. Top moments of RCB Unbox | Bold Diaries - Royal Challengers Bangalore
8. Punjab Kings: Another new captain and coach for a new season - ESPNcricinfo
9. Watch: Rohit's telling reaction, MI's act of gold as Harmanpreet and Co. win WPL - Hindustan Times
10. Women's World Boxing Championships: Gold glory for India as all 4 boxers win gold - Times of India
11. IPL 2023's "Best Bowling Attack Belongs To...": Ex-India Star's Blunt Take. It's Not MI Or CSK - NDTV Sports
12. Will Chepauk return help CSK spin it to win it? - ESPNcricinfo
13. BCCI Central Contracts: Injuries force BCCI hand, Shikhar Dhawan, Sanju Samson given World Cup squad backdoor before IPL 2023- Check out - InsideSport
14. Medvedev Handed Walkover Into Miami Fourth Round - ATP Tour
15. Tottenham boss Antonio Conte leaves after mutual agreement - ESPN India
16. LeBron James back for Lakers after missing 13 games for foot - ESPN India
17. Luxembourg 0-6 Portugal: Player ratings for the Selecao as another Cristiano Ronaldo brace leads to big win | UEFA Euro 2024 qualifiers - Sportskeeda
18. Barcelona Has One Key Move to Overcome Financial Hurdle of Signing Messi, per Report - PSG Talk
19. Carlos Alcaraz Reaches Fourth Round In Miami - ATP Tour
20. Mumbai win inaugural WPL as Lanning's Delhi fall short - cricket.com.au



