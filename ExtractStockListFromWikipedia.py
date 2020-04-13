# import required libraries
import pandas as pd
# enter the URL of the Wikipedia page
table = pd.read_html('https://en.wikipedia.org/wiki/List_of_BSE_SENSEX_companies')
# extract the table
df = table[0]
# to create two different csv files 1.info 2.exchange tickers
df.to_csv('Sensex-Info.csv')
df.to_csv("Sensex-Tickers.csv", columns=['Exchange ticker'])
