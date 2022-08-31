import requests
from newsapi import NewsApiClient
from twilio.rest import Client

newsapi = NewsApiClient(api_key='a23ca30af79b4bfbaa1ea5630f8f5ce8')
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
TWILIO_SID = "ACb55e64befd991304125b5fb64fa46175"
TWILIO_AUTH_TOKEN="6d5eaf0f2df5cdf443288f1d8b25344a"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters={
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "OWDG1502GPBCMYT1",
}

parameters_news= { "q":'tesla',
                   "from": "2022-06-05",
                   "sortBy":"publishedAt",
                   "apiKey":"a23ca30af79b4bfbaa1ea5630f8f5ce8"

}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = response.json()
# print(data)
yesterday_closing_stock = 0
day_before_yesterday_closing_stock = 0
for key, values in data.items():
    yesterday_closing_stock = data["Time Series (Daily)"]["2022-07-01"]["4. close"]
    day_before_yesterday_closing_stock = data["Time Series (Daily)"]["2022-06-30"]["4. close"]


positive_difference = abs(float(yesterday_closing_stock)-float(day_before_yesterday_closing_stock))

percentage_bt_two = ((float(yesterday_closing_stock))-positive_difference) / 100

if percentage_bt_two > 5:
    response_news = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
    data_news = response_news.json()["articles"]
    three_articles = data_news[:3]
    print(three_articles)
    formated_article_list = [f"Headline:{article['title']}.\nBrief:{article['description']}"for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formated_article_list:
        message = client.messages \
            .create(
                     body=article,
                     from_='+19805258168',
                     to='+32467606413'
        )

        print(message.status)



    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

