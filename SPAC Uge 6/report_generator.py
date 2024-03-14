from data_analyser import Analyser
from data_reader import df_salesdata
from data_visualiser import Plots
import pandas as pd
import matplotlib.pyplot as plt

Plots.sales_over_time_plot(df_salesdata).savefig('Sales over Time all products.png')
Plots.cumulative_sales_plot(df_salesdata)
print('Salget i virksomheden er forholdsvis stabilt, som kan ses af "Cumulative Sales.png", som viser en linær inkomst over tid.')
print('Som I kan se i plottet "Sales over Time all products.png", er der fluktuering i salget, men det ligger generelt pænt omkring 40.000.')
print('Fra efteråret 2021 og frem til foråret 2023, havde vi de størte udsving med både de højeste og laveste salgsmåneder i årtiet.')
print('Det kunne være værd at kigge nærmere på 2022 i forhold til andre år.\n \n')

def product_filter(df, product):
    return df[df['Product']== product]

dress = product_filter(df_salesdata, 'Dress')
jacket = product_filter(df_salesdata, 'Jacket')
jeans = product_filter(df_salesdata, 'Jeans')

print(pd.concat([Analyser.total_sales(df_salesdata,['Product'])[0], 
                 df_salesdata.groupby('Product', observed = True)['Units Sold'].sum()],
                 axis= 1))

print('Den ovenstående tabel viser, at vi har solgt nogenlunde det samme antal af hvert produkttype,')
print('men at vi ikke overraskende får klart mest ind for jakker og kjoler og ikke ret meget for sokker og hatte.')
print(f'Vores top 5 bedst sælgende produkter, i forhold til salgspris er {Analyser.top_x_price(df_salesdata)},')
print(f'mens de top 5 bedst sælgende i forhold til antal solgte er {Analyser.top_x_units(df_salesdata)}')
print('Der er ikke den store variation i units solgt, men der er en markant difference i hvor meget vi har tjent.')
print('Vi tjekker graferne for top tre bedst sælgende produkter, for at se hvor stor deres inflydelse var på vores generalle salg.')
Plots.sales_over_time_plot(jacket).savefig('Sales over Time jackets.png')
Plots.sales_over_time_plot(dress).savefig('Sales over Time dress.png')
Plots.sales_over_time_plot(jeans).savefig('Sales over Time jeans.png')
print('Salget af især jakker er meget bølgende. De to laveste måneder i vores overall salg er der også nedgang i jakke salget,')
print('men ikke noget ud over det sedvanlige. Tilgengæld har kjoler deres værste måned i marts 2023, hvilket svarer til vores overordnede dårligste')
print('måned. Jeans har deres værste måned i februar 2022, hvilket er vores næstdårligste måned.')
print('Det ville derfor være en god ide, at kigge nærmere på disse tre produkter, og se hvad der kan gøres,')
print('for at de har et mere stabilt højt salg i fremtiden.\n \n')
Plots.gender_dist_plot(df_salesdata)
print('Med hensyn til kænsfordelingen af vores tøj, viser tallene at vi sælger klart mest herrertøj,')
print('mens vi stort set intet børnetøj sælger. Overvej derfor, om der skal gøres noget for at forbedre salget,')
print('eller om det ville være bedre helt at droppe børnetøj for at fokusere mere på tøj til voksne.')
