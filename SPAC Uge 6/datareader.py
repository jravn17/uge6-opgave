import pandas as pd

df_salesdata = pd.read_csv('tøjfirma_sales_data.csv', sep=',')

# Tilføjer så vi sikre vi har indlæst kolonnerne korekt
df_salesdata.columns = ['Product','Category','Size','Units Sold', 'Sale Price', 'Sale Date']

# Fjerner duplikater i filen
df_salesdata.drop_duplicates(inplace=True)

# Fjern rækker med manglende eller ugyldige værdier
df_salesdata.dropna(subset=['Product','Category','Size','Units Sold', 'Sale Price', 'Sale Date'], inplace=True)

#Konvertering 'Product_Type' og 'Weather'  kolonner til kategorisk værdi
df_salesdata['Product'] = df_salesdata['Product'].astype('category')
df_salesdata['Category'] = df_salesdata['Category'].astype('category')
df_salesdata['Size'] = df_salesdata['Size'].astype('category')

# Konvertering kolonner til numeriske værdier
df_salesdata['Units Sold'] = df_salesdata['Units Sold'].astype(int)
df_salesdata['Sale Price'] = df_salesdata['Sale Price'].astype(float)

#Konvertering 'Date' kolonne til datetime format
df_salesdata['Sale Date'] = pd.to_datetime(df_salesdata['Sale Date'])

#print(df_salesdata)
