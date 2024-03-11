import pandas as pd
from datareader import df_salesdata

def total_sales(df, filters = []):
    if not filters:
        try:
            return df['Sale Price'].sum()
        except ValueError:
            pass
    else:
        try:
            sales = df.groupby(filters)['Sale Price'].sum()
            return sales
        except ValueError:
            pass
        except KeyError:
            print('Incorrect filter applied')



def avg_sales(df,filters =[]):
    if not filters:
        try:
            return df['Sale Price'].mean()
        except ValueError:
            pass
    else:
        try:
            sales = df.groupby(filters)['Sale Price'].mean()
            return sales
        except ValueError:
            pass
        except KeyError:
            print('Incorrect filter applied')
            

def top_x_units(df, x=5):
    return df.groupby('Product')['Units Sold'].sum().nlargest(x)

def top_x_price(df, x=5):
    return df.groupby('Product')['Sale Price'].sum().nlargest(x)

def gender(df):
        return df.groupby('Category')['Units Sold'].sum()
    
def sales_over_time(df):
   # Antag at du har en kolonne 'date' i din DataFrame
    df['Sale Date'] = pd.to_datetime(df['Sale Date'])
# Du kan analysere salgsmønstre pr. måned for at identificere sæsonmæssige trends
    monthly_sales = df_salesdata.groupby(df_salesdata['date'].dt.month)['sales_amount'].sum()
    #monthly_sales.plot(kind='bar', xlabel='Måned', ylabel='Salgsmængde', title='Salgsmønstre pr. måned') 

    

