import pandas as pd
table = pd.read_html('https://en.wikipedia.org/wiki/List_of_BSE_SENSEX_companies')
df = table[0]
df.to_csv('Sensex-Info.csv')
df.to_csv("Sensex-Tickers.csv", columns=['Exchange ticker'])