from data_analyser import Analyser
from data_reader import df_salesdata
from data_visualiser import Plots
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
        total_sales_amount, total_transactions = Analyser.total_sales(df_salesdata)
        print("Total Salg:", total_sales_amount)
        print("Total Transaktioner:", total_transactions)
    elif choice == '2':
        print("Gennemsnitlig salg:", Analyser.avg_sales(df_salesdata))
    elif choice == '3':
        print("Top 5 Units Solgt:")
        print(Analyser.top_x_units(df_salesdata))
    elif choice == '4':
        print("Top 5 Priser:")
        print(Analyser.top_x_price(df_salesdata))
    elif choice == '5':
        print("Kønsfordeling:")
        print(Analyser.gender(df_salesdata))

    elif choice == '6':
        print("Salg Over Tid:")
        print(Analyser.sales_over_time_plot(df_salesdata))
    elif choice == '7':
        print("Vælg plot")
        print("1) Salg over tid")
        print("2) Kumulative salg")
        print("3) Salg per produkt")
        print("4) Salgspris distribution")
        print("5) Salgspris distribution per produkt")
        print("6) Kønsfordeling")
        print("7) Quit")
        plot_choice = input("Enter your choice: ").strip()
        if plot_choice == '1':
            Plots.sales_over_time_plot(df_salesdata)
        elif plot_choice == '2':
            Plots.cumulative_sales_plot(df_salesdata)
        elif plot_choice == '3':
            Plots.sales_of_topselling_product_plot(df_salesdata)
        elif plot_choice == '4':
            Plots.sales_price_dist_plot(df_salesdata)
        elif plot_choice == '5':
            Plots.price_dist_by_products_plot(df_salesdata)
        elif plot_choice == '6':
            Plots.gender_dist_plot(df_salesdata)
        elif plot_choice == '7':
            break
        else:
            print("Invalid choice")
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid valg, skriv venligt et nummer mellem 1-8")
