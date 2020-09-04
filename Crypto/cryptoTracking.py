import pandas_datareader as pdr
from datetime import *
import time
import matplotlib.pyplot as plt
import pandas as pd

end_date = datetime.now()
start_date = datetime(2020, 1, 1)
BTC = pdr.DataReader(name="BTC-USD", data_source="yahoo", start = start_date, end = end_date)
ETH = pdr.DataReader("ETH-USD", "yahoo", start_date, end_date)
print(BTC[['Close','High']])
print(ETH['Close'])

ma_days = [13,34]
for ma in ma_days:
    col_name = "MA %s days" %(str(ma))
    BTC[col_name] = BTC['Close'].rolling(window=ma).mean()

BTC[['Close','MA 13 days', 'MA 34 days']].plot(grid=True)
plt.show()
   
