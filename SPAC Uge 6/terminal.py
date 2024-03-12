from data_analyser import *
from datareader import *
from data_visualiser import *
import matplotlib.pyplot as plt
import os





#we are not gonna do math on these numbers
while True:
    print("1) Total Salg")
    print("2) Gennemsnitlig Salg")
    print("3) Top 5 Units Solgt")
    print("4) Top 5 Price ")
    print("5) Kønsfordeling")
    print("6) Salg over tid")
    print("7) Plots")
    print("8) Quit")
    
    choice = input("Enter your choice: ")
    
    choice = choice.strip()

    if choice == '1':
        total_sales_amount, total_transactions = total_sales(df_salesdata)
        print("Total Salg:", total_sales_amount)
        print("Total Transaktioner:", total_transactions)
    elif choice == '2':
        print("Gennemsnitlig salg:", avg_sales(df_salesdata))
    elif choice == '3':
        print("Top 5 Units Solgt:")
        print(top_x_units(df_salesdata))
    elif choice == '4':
        print("Top 5 Priser:")
        print(top_x_price(df_salesdata))
    elif choice == '5':
        print("Kønsfordeling:")
        print(gender(df_salesdata))

    elif choice == '6':
        print("Salg Over Tid:")
        print(sales_over_time_plot(df_salesdata))
    elif choice == '7':
        print("Vælg plot")
        print("1) Sales over Time")
        print("2) Cumulative Sales")
        print("3) Sales of Top Selling Product")
        print("4) Sales Price Distribution")
        print("5) Price Distribution by Products")
        print("6) Gender Distribution")
        print("7) Quit")
        plot_choice = input("Enter your choice: ").strip()
        if plot_choice == '1':
            sales_over_time_plot(df_salesdata)
        elif plot_choice == '2':
            cumulative_sales_plot(df_salesdata)
        elif plot_choice == '3':
            sales_of_topselling_product_plot(df_salesdata)
        elif plot_choice == '4':
            sales_price_dist_plot(df_salesdata)
        elif plot_choice == '5':
            price_dist_by_products_plot(df_salesdata)
        elif plot_choice == '6':
            gender_dist_plot(df_salesdata)
        elif plot_choice == '7':
            break
        else:
            print("Invalid choice")
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid valg, skriv venligt et nummer mellem 1-8")
