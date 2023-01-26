import requests

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

STOCK_API_KEY = '89676MTP5OPIJF4J'

#################
stock_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()
data_list = [value for (key, value) in data.items()]

yester_data = data_list[0]
yester_closing_prince = yester_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = abs(float(yester_closing_prince) - float(day_before_yesterday_closing_price))
diff_percent = difference / yester_closing_prince

if diff_percent > 4:
    print('get news')