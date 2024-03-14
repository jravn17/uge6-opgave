from data_analyser import Analyser
from datareader import df_salesdata , DataReader
from data_visualiser import Plots

df_salesdata = DataReader.load_data(df_salesdata)

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
        print("1. For et specifikt år")
        print("2. For alle år")
        choice_year = input("Vælg option: ").strip()
        if choice_year == '1':
            year = int(input("Indtast et årstal mellem 2020-2024: "))
            if year < 2020 or year > 2024:
                print("Ugyldigt årstal. Prøv igen.")
            else:
                top_categories = Analyser.top_x_price(df_salesdata, year)
                print(f"De fem mest solgte produktkategorier for år {year} er:")
                for i, category in enumerate(top_categories, start=1):
                    print(f"{i}. {category}")
        elif choice_year == '2':
            top_categories_all_years = Analyser.top_x_price(df_salesdata, year = None)
            print("De fem mest solgte produktkategorier for alle år er:")
            for i, category in enumerate(top_categories_all_years, start=1):
                print(f"{i}. {category}")
            else:
                print("Ugyldigt valg. Vælg enten 1 eller 2.")
    elif choice == '5':
        print("Kønsfordeling:")
        print(Analyser.gender(df_salesdata))

    elif choice == '6':
        print("Salg Over Tid:")
        print(Analyser.sales_over_time_plot(df_salesdata))
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
