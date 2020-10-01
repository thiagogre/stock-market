import requests
import pandas as pd

api_key = 'GMIFJYYVMLZTZVHA'

symbol = input(str(
    'What symbol you desire search?\n"MSFT, AAPL, AMZN, GOOG, FB, INTC, CSCO, CMCSA, PEP, ADBE, NVDA, NFLX"\nType: '))
symbol = symbol.upper()

request_json = requests.get(
    f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}')

company_overview = request_json.json()

company_overview_title = []
company_overview_description = []

for key in company_overview.keys():
    company_overview_title.append(key)
    company_overview_description.append(company_overview[f'{key}'])

pd.DataFrame({'TITLE': company_overview_title, 'DESCRIPTION': company_overview_description}).to_excel(
    'excel_files/company_overview.xlsx')
