import pandas as pd
import sys

# Tickers
exchange = sys.argv[1]
fulldata = pd.read_csv('CafeF.'+exchange+'.Upto06.04.2023.csv')
fulldata = (fulldata.rename(columns = {'<Ticker>':'ticker','<DTYYYYMMDD>':'Date','<Open>':'Open','<High>':'High','<Low>':'Low','<Close>':'Close','<Volume>':'Volume'}))
ticklist = sys.argv[2:]
path = '.\\tickers\\'
for tick in ticklist:
    tickData = fulldata[fulldata.ticker==tick]
    tickData = tickData.drop_duplicates()
    tickData.to_csv(path+tick+".csv",columns=['Date','Open','High','Low','Close','Volume'], index=False)
    print(tickData)

# Data source: 
# arg1 arg2
# <market> <stock code>
# INDEX <market code>