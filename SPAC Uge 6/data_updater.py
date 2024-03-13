from faker import Faker
import pandas as pd

fake = Faker()

df_salesdata = pd.read_csv('tøjfirma_sales_data.csv', sep=',')

date = pd.Series([fake.date_time_this_decade() for x in range(len(df_salesdata))])
df_salesdata['Sale Date'] = date

units = pd.Series([fake.pyint(min_value=1, max_value=5) for x in range(len(df_salesdata))])
df_salesdata['Units Sold'] = units

df_salesdata.to_csv('bedre_sales_data.csv', sep=',')