from data_analyser import *
import matplotlib.pyplot as plt

def sales_over_time_plot(df):
    sales_per_day = sales_over_time(df)
    fig, axs = plt.subplots()
    sales_per_day.plot(ax = axs)
    axs.set_xlabel('Date')
    axs.set_ylabel('Income')
    fig.savefig('Sales over Time.png')
    return fig

def cumulative_sales_plot(df):
    cumulative = cumulative_sales(df)
    fig, axs = plt.subplots()
    cumulative.plot.area(ax = axs)
    axs.set_xlabel('Time')
    axs.set_ylabel('Cumulative Income')
    fig.savefig('Cumulative Sales.png')
    return fig

def sales_of_topselling_product_plot(df, x = 10):
    sales_per_product = top_x_price(df,x)
    number_of_product = top_x_units(df,x)
    fig, axs = plt.subplots()
    pd.concat([sales_per_product, number_of_product], axis = 1).plot.bar(ax=axs)
    fig.savefig(f'Sales by {x} best-selling Product.png')
    return fig

def sales_price_dist_plot(df):
    fig,axs = plt.subplots()
    df['Sale Price'].plot.box(ax = axs)
    axs.set_ylabel('Price')
    fig.savefig('Box-plot of price dist.png')
    return fig


def price_dist_by_products(df):
    fig, axs = plt.subplots()
    pivoted = pd.pivot(df_salesdata,columns='Product', values = 'Sale Price')
    pivoted.plot.box(ax = axs)
    axs.set_ylabel('Price')
    fig.savefig('Box-plots of price distribution by category.png')
    return fig



