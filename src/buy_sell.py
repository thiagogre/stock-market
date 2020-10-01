from alpha_vantage.timeseries import TimeSeries
import numpy as np
import pandas as pd
from utils.graphics import graphic_last_month
from utils.date import last_day_of_last_month

# 5 calls/min and 500 calls/day
api_key = 'GMIFJYYVMLZTZVHA'

ts = TimeSeries(key=api_key, output_format='pandas')

symbol = input(str(
    'What symbol you desire search?\n"MSFT, AAPL, AMZN, GOOG, FB, INTC, CSCO, CMCSA, PEP, ADBE, NVDA, NFLX"\nType: '))
symbol = symbol.upper()

# LAST WEEK INTRADAY
data_intraday, meta_data_intraday = ts.get_intraday(
    symbol=f'{symbol}', interval='1min', outputsize='full')

last_month = last_day_of_last_month()

data_last_week = data_intraday.loc[data_intraday.index >=
                                   f'{last_month[3]}-{last_month[1]}-{last_month[2]} 00:00:00']

np_last_week = np.array(data_last_week)

last_week_low_prices = np.sort(np_last_week[:, 2])
last_week_100_low_prices = last_week_low_prices[0:100]
last_week_100_low_prices_average = np.mean(last_week_100_low_prices)
last_week_100_low_prices_average_round = round(
    last_week_100_low_prices_average, 2)
pd.DataFrame({'Low Price': last_week_100_low_prices}
             ).to_excel('excel_files/low-100.xlsx')
graphic_last_month(last_week_100_low_prices, 'Low')

last_week_high_prices = np.sort(np_last_week[:, 1])
last_week_high_prices_reverse = last_week_high_prices[::-1]
last_week_100_high_prices = last_week_high_prices_reverse[0:100]
last_week_100_high_prices_average = np.mean(last_week_100_high_prices)
last_week_100_high_prices_average_round = round(
    last_week_100_high_prices_average, 2)
pd.DataFrame({'High Price': last_week_100_high_prices}
             ).to_excel('excel_files/high.xlsx')
graphic_last_month(last_week_100_high_prices, 'High')

print(
    f'Average 100 PRICES LAST WEEK -> HIGH: {last_week_100_high_prices_average_round}, LOW: {last_week_100_low_prices_average_round}')

data_last_day = data_intraday.loc[data_intraday.index >=
                                  f'{last_month[3]}-{last_month[4]}-{last_month[5]} 00:00:00']

data_last_day_high = np.array(data_last_day['2. high'])
data_last_day_low = np.array(data_last_day['3. low'])

buy = []
sell = []

for price in (list(data_last_day_high)):
    if price > last_week_100_high_prices_average_round:
        sell.append(price)

for price in (list(data_last_day_low)):
    if price < last_week_100_low_prices_average_round:
        buy.append(price)

print(f'BOUGHT: {buy}, SELL: {sell}')
