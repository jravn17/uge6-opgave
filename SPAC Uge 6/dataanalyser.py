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

def gender(df, category=None):
    if category:
        if category.lower() in ['men', 'women', 'children']:
            gender_distribution = df[df['Category'].str.lower() == category.lower()]['Units Sold'].sum()
            return {category: gender_distribution}
        else:
            print("Invalid gender category. Please enter 'Men', 'Women', or 'Children'.")
            return None  
    else:
        gender_distribution = df.groupby('Category')['Units Sold'].sum()
        return gender_distribution
    
def sales_over_time(df):
    return df.groupby(df['Sale Date'].dt.date)['Sale Price'].sum()

def cumulative_sales(df):
    return sales_over_time(df).cumsum() 

    

