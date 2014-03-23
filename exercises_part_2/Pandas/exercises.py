# coding=utf-8
import pandas as pd
import pandas.io.data as web
import datetime as dt
import matplotlib.pyplot as plt

__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1 - Stock price changes since beginning this year :'
start_date = dt.date(2014, 01, 01)
end_date = dt.date.today()
ticker_list = {'INTC': 'Intel',
               'MSFT': 'Microsoft',
               'IBM': 'IBM',
               'BHP': 'BHP',
               'RSH': 'RadioShack',
               'TM': 'Toyota',
               'AAPL': 'Apple',
               'AMZN': 'Amazon',
               'BA': 'Boeing',
               'QCOM': 'Qualcomm',
               'KO': 'Coca-Cola',
               'GOOG': 'Google',
               'SNE': 'Sony',
               'PTR': 'PetroChina'}

web_data = web.DataReader(ticker_list.keys(), "yahoo", start_date, end_date)
start_price = web_data.iloc[:, 0, :].Close
curr_price = web_data.iloc[:, -1, :].Close
price_change = (curr_price-start_price)/start_price*100
price_change.index = [ticker_list[abbr] for abbr in price_change.index]
price_change.sort()
price_change.plot(kind='bar')
plt.show()
#endregion
