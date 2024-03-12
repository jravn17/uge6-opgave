import pandas as pd
from datareader import df_salesdata

def total_sales(df):
    try:
        return df['Sale Price'].sum()
    except ValueError:
        pass
        
def avg_sales(df):
    try:
        return df['Sale Price'].mean()
    except ValueError:
        pass
            
def top_x_units(df, x=5):
    return df.groupby('Product')['Units Sold'].sum().nlargest(x)

def top_x_price(df, x=5):
    return df.groupby('Product')['Sale Price'].sum().nlargest(x)

def gender(df):
        return df.groupby('Category')['Units Sold'].sum()
    
def sales_over_time(df):
    return df.groupby(df['Sale Date'].dt.date)['Sale Price'].sum()

def cumulative_sales(df):
    return sales_over_time(df).cumsum() 

    

