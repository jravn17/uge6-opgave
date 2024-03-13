from data_analyser import Analyser
from data_reader import df_salesdata
from data_visualiser import Plots
import pandas as pd

Plots.sales_over_time_plot(df_salesdata)
print('Salget i virksomheden er forholdsvis stabilt.')
print('Som I kan se i plottet "Sales over Time.png", er der fluktuering i salget, men det ligger generelt pænt omkring 40.000.')
print('Fra efteråret 2021 og frem til foråret 2023, havde vi de størte udsving med både de højeste og laveste salgsmåneder i årtiet.')
print('Det kunne være værd at kigge nærmere på 2022 i forhold til andre år.\n \n')

def product_filter(df, product):
    return df[df['Product']== product]

dress = product_filter(df_salesdata, 'Dress')
hat = product_filter(df_salesdata, 'Hat')
hoodie = product_filter(df_salesdata, 'Hoodie')
jacket = product_filter(df_salesdata, 'Jacket')
jeans = product_filter(df_salesdata, 'Jeans')
shorts = product_filter(df_salesdata, 'Shorts')
skirt = product_filter(df_salesdata, 'Skirt')
socks = product_filter(df_salesdata, 'Socks')
sweater = product_filter(df_salesdata, 'Sweater')
t_shirt = product_filter(df_salesdata, 'T-Shirt')

print(pd.concat([Analyser.total_sales(df_salesdata,['Product'])[0], 
                 df_salesdata.groupby('Product', observed = True)['Units Sold'].sum()],
                 axis= 1))

print('Den ovenstående tabel viser, at vi har solgt nogenlunde det samme antal af hvert produkttype,')
print('men at vi ikke overraskende får klart mest ind for jakker og kjoler og ikke ret meget for sokker og hatte.')
print(f'Vores top 5 bedst sælgende produkter, i forhold til salgspris er {Analyser.top_x_price},')
print(f'mens de top 5 bedst sælgende i forhold til antal solgte er {Analyser.top_x_units}')
print('Vi tjekker hvor stor en korrolation de fem sælgende produkter, med hensyn til pris, har haft med de flukturenede priser.')
print('Her viser graferne')