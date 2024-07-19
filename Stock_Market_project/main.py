import requests
import datetime
import math
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def news():
    api_response = requests.get("https://newsapi.org/v2/everything?q=apple&from=2024-01-01&to=2024-01-01&sortBy=popularity&apiKey=19a967aee7d346e0bb039a2d2c3c2dc6")
    json_data = api_response.json()

    if 'articles' in json_data:
        articles = json_data['articles'][:3]

        for article in articles:
            author = article.get('author')
            title = json_data.get('title')
            description = article.get('description')
            date = article.get('publishedAt')

    print(f"Author: {author}, Title : {title}, Description: {description}, Date : {date}" )

def stocks():
    api_stock_response = requests.get('https://api.polygon.io/v1/open-close/AAPL/2023-12-28?adjusted=true&apiKey=gtOZiR7Qy98hz1wW4bFhm8U6aoDAceSo')
    prev_api_response = requests.get('https://api.polygon.io/v2/aggs/ticker/AAPL/prev?adjusted=true&apiKey=gtOZiR7Qy98hz1wW4bFhm8U6aoDAceSo')
    json_data = api_stock_response.json()
    prev_json_data = prev_api_response.json()

    current_opening_value = json_data['open']
    current_closing_value = json_data['close']

    previous_opening_value = prev_json_data['results'][0]['o']
    previous_closing_value = prev_json_data['results'][0]['c']
    growth_percentage = math.floor(((current_opening_value - previous_closing_value)/ previous_closing_value) * 100)

    print(f"Opening Value : {current_opening_value}, Closing Value : {current_closing_value}")
    print(f"Opening Value : {previous_opening_value}, Closing Value : {previous_closing_value}")
    print(f"Stock Growth : {growth_percentage}")
    


print(stocks())


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

