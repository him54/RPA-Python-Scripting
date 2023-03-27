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


