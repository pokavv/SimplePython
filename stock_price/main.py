import requests
from twilio.rest import Client

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'IBM'

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
STOCK_API_KEY = '89676MTP5OPIJF4J'
NEWS_API_KEY = '33e653afbf9941ed92a521fef9beae22'

TWILIO_SID = 'SID'
TWILIO_AUTH_TOKEN = 'AUTH TOKEN'

###########################################

stock_param = {
    'function': 'TIME_SERIES_WEEKLY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_param)
data = response.json()['Weekly Time Series']
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price  = yesterday_data['4. close']
print(f'어제 {STOCK_NAME} 종가 = {yesterday_closing_price}')

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(f'엊그제 {STOCK_NAME} 종가 = {day_before_yesterday_closing_price}')

diff = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
diff_percent = (diff / float(yesterday_closing_price)) * 100
print(f'주가 변동 = {round(diff, 2)}$')
print(f'증감률 = {round(diff_percent, 2)}%')

############################################

if diff_percent >= 2 or diff_percent <= -2:
    news_params = {
        'apikey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles'][:3]
    print(articles)

############################################

formatted_articles = [f'Headline: {articles["title"]}. \nBrief: {articles["description"]}' for article in articles]
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_='+phone number',
        to='your_number_here'
    )