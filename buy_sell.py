from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date

today = date.today()
print("Today's date:", today)

# 5 calls/min and 500 calls/day
api_key = 'GMIFJYYVMLZTZVHA'

ts = TimeSeries(key=api_key, output_format='pandas')

symbol = input(str(
    'What symbol you desire search?\n"MSFT, AAPL, AMZN, GOOG, FB, INTC, CSCO, CMCSA, PEP, ADBE, NVDA, NFLX"\nType: '))
symbol = symbol.upper()


# LAST MONTH INTRADAY
data_intraday, meta_data_intraday = ts.get_intraday(
    symbol=f'{symbol}', interval='1min', outputsize='full')

data_last_month = data_intraday.loc[data_intraday.index >=
                                    '2020-09-01 00:00:00']
np_last_month = np.array(data_last_month)

last_month_low_prices = np.sort(np_last_month[:, 2])
last_month_100_low_prices = last_month_low_prices[0:100]
last_month_100_low_prices_average = np.mean(last_month_100_low_prices)
last_month_100_low_prices_average_round = round(
    last_month_100_low_prices_average, 2)
pd.DataFrame({'Low Price': last_month_100_low_prices}).to_excel('low-100.xlsx')
plt.plot(last_month_100_low_prices)
plt.show()

last_month_high_prices = np.sort(np_last_month[:, 1])
last_month_high_prices_reverse = last_month_high_prices[::-1]
last_month_100_high_prices = last_month_high_prices_reverse[0:100]
last_month_100_high_prices_average = np.mean(last_month_100_high_prices)
last_month_100_high_prices_average_round = round(
    last_month_100_high_prices_average, 2)
pd.DataFrame({'High Price': last_month_100_high_prices}
             ).to_excel('high-100.xlsx')
plt.plot(last_month_100_high_prices)
plt.show()

print(
    f'Average 100 PRICES LAST MONTH -> HIGH: {last_month_100_high_prices_average_round}, LOW: {last_month_100_low_prices_average_round}')

data_day = data_intraday.loc[data_intraday.index >=
                             '2020-09-29 00:00:00']

data_day_high = np.array(data_day['2. high'])
data_day_sell = np.array(data_day['3. low'])

buy = []
sell = []

for price in (list(data_day_high)):
    if price > last_month_100_high_prices_average_round:
        sell.append(price)

for price in (list(data_day_sell)):
    if price < last_month_100_low_prices_average_round:
        buy.append(price)

print(f'BOUGHT: {buy}, SELL: {sell}')
