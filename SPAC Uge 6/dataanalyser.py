
class Analyser:

    @staticmethod
    def total_sales(df, filters = []):
        if not filters:
            try:
                return df['Sale Price'].sum(), len(df)
            except ValueError as e:
                return None, e
        else:
            try:
                sales = df.groupby(filters, observed=True)['Sale Price'].sum()
                return sales, len(sales)
            except (ValueError, KeyError) as e:
                return None, e
 
    @staticmethod
    def avg_sales(df, filters =[]):
        if not filters:
            try:
                return df['Sale Price'].mean(), len(df)
            except ValueError as e:
                return None, e
        else:
            try:
                sales = df.groupby(filters, observed=True)['Sale Price'].mean()
                return sales, len(sales)
            except (ValueError, KeyError) as e:
                return None, e
            
    @staticmethod
    def top_x_units(df, x=5):
        return df.groupby('Product', observed = True)['Units Sold'].sum().nlargest(x)

    @staticmethod
    def top_x_price(df, n=5):
         if year:
            df_year = df[df['Sale Date'].dt.year == year]
        else:
            df_year = df
        top_categories = df_year.groupby('Product')['Sale Price'].sum().nlargest(n).index.tolist()
        return top_categories

    @staticmethod
    def gender(df):
        return df.groupby('Category', observed = True)['Units Sold'].sum()
    
    @staticmethod
    def sales_over_time(df,):
        return df.groupby([df['Sale Date'].dt.year.values,
                            df['Sale Date'].dt.month.values], observed = True)['Sale Price'].sum()
        
    @staticmethod
    def cumulative_sales(df):
        return Analyser.sales_over_time(df).cumsum() 
     
    

