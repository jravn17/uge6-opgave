from dataanalyser import *
from datareader import *

#we are not gonna do math on these numbers
while True:
    print("1) Total Sales)")
    print("2) Average Sales")
    print("3) Top 5 Units Sold")
    print("4) Top 5 Price ")
    print("5) Top 5 Gender Distribution")
    print("6) Sales Over Time")
    print("7) Quit")
    
    choice = input("Enter your choice: ")
    
    choice = choice.strip()

    if choice == '1':
        total_sales_amount, total_transactions = total_sales(df_salesdata)
        print("Total Sales:", total_sales_amount)
        print("Total Transactions:", total_transactions)
    elif choice == '2':
        print("Average Sales:", avg_sales(df_salesdata))
    elif choice == '3':
        print("Top 5 Units Sold:")
        print(top_x_units(df_salesdata))
    elif choice == '4':
        print("Top 5 Price:")
        print(top_x_price(df_salesdata))
    elif choice == '5':
        print("Gender Distribution:")
        category = input("Skriv køn til udvælgelse (Women, Men, Children, eller Vis Alle): ")  
        if category.lower() == 'vis alle':
            print(gender(df_salesdata))
        elif category.lower() in ['men', 'women', 'children']:
            print("Gender Distribution for all categories:")
            print(gender(df_salesdata,category))
        else:
            print("Invalid køns kategori. Please enter 'Men', 'Women', or 'Children'.")
    elif choice == '6':
        print("Sales Over Time:")
        sales_over_time(df_salesdata) 
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid valg, skriv venligt et nummer mellem 1-7")
