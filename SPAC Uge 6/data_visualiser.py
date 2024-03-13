from data_analyser import Analyser
import matplotlib.pyplot as plt
import pandas as pd

class Plots:

    @staticmethod
    def sales_over_time_plot(df):
        sales_per_month = Analyser.sales_over_time(df)
        fig, axs = plt.subplots()
        sales_per_month.plot(ax = axs)
        plt.title('Sales over Time')
        axs.set_xlabel('Date')
        axs.set_ylabel('Income')
        fig.autofmt_xdate()
        plt.tight_layout()
        fig.savefig(f'Sales over Time {df}.png')
        return fig

    @staticmethod
    def cumulative_sales_plot(df):
        cumulative = Analyser.cumulative_sales(df)
        fig, axs = plt.subplots()
        cumulative.plot.area(ax = axs)
        axs.set_xlabel('Time')
        axs.set_ylabel('Cumulative Income')
        fig.autofmt_xdate()
        plt.tight_layout()
        fig.savefig('Cumulative Sales.png')
        return fig

    @staticmethod
    def sales_of_topselling_product_plot(df, x = 10):
        sales_per_product = Analyser.top_x_price(df,x)
        number_of_product = Analyser.top_x_units(df,x)
        fig, axs = plt.subplots()
        pd.concat([sales_per_product, number_of_product], axis = 1).plot.bar(ax=axs)
        plt.tight_layout()
        fig.savefig(f'Sales by {x} best-selling Product.png')
        return fig

    @staticmethod
    def sales_price_dist_plot(df):
        fig,axs = plt.subplots()
        df['Sale Price'].plot.box(ax = axs)
        axs.set_ylabel('Price')
        plt.tight_layout()
        fig.savefig('Box-plot of price dist.png')
        return fig


    @staticmethod
    def price_dist_by_products_plot(df):
        fig, axs = plt.subplots()
        pivoted = pd.pivot(df,columns='Product', values = 'Sale Price')
        pivoted.plot.box(ax = axs)
        plt.tight_layout()
        axs.set_ylabel('Price')
        fig.savefig('Box-plots of price distribution by category.png')
        return fig

    @staticmethod
    def gender_dist_plot(df):
        fig, axs = plt.subplots()
        data = df.groupby('Category', observed=True)['Units Sold'].sum()
        data.plot.bar(ylim=(data.min()-(data.max()-data.min())/10, data.max()+(data.max()-data.min())/10))
        axs.set_ylabel('Units')
        plt.tight_layout()
        fig.savefig('Bar-chart of transactions by gender.png')
        return fig

