class Analyser:

    @staticmethod
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


    @staticmethod
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
            
    @staticmethod
    def top_x_units(df, x=5):
        return df.groupby('Product')['Units Sold'].sum().nlargest(x)

    @staticmethod
    def top_x_price(df, x=5):
        return df.groupby('Product')['Sale Price'].sum().nlargest(x)

    @staticmethod
    def gender(df):
        return df.groupby('Category')['Units Sold'].sum()
    
    @staticmethod
    def sales_over_time(df):
        return df.groupby(df['Sale Date'].dt.date)['Sale Price'].sum()

    @staticmethod
    def cumulative_sales(df):
        return Analyser.sales_over_time(df).cumsum() 
    

