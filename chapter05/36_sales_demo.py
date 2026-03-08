from functools import reduce

def main():
    
    months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
    ]

    sales = [
    12_000, 15_500, 13_200, 18_000,
    21_300, 19_800, 24_500, 23_000,
    20_600, 22_100, 25_400, 27_000
    ]

    # create a new dictionary with months and sales --> January : 12_000
    
    my_dict = {}
    for i , month in enumerate(months):
        my_dict[month] = sales[i]
    print(my_dict)
        
    print('-' * 50)
    
    monthly_sales = dict(zip(months , sales))
    print(monthly_sales)
    
    print('-' * 50)
    for month , value in monthly_sales.items():
        print(f"{month:<9} : {value:>6}K")
        
    print('-' * 50)
    
    print("Months with sales >= 15000")
    
    high_sales_months = {month : value for month , value in monthly_sales.items() if value >= 22_000 }
    high_sales_months_2 = dict(filter(lambda month_tuple : month_tuple[1] >= 22_000 , monthly_sales.items()))
    print(high_sales_months)
    print(high_sales_months_2)
    
    print("Apply discount of 10 per cent for all sales >= 18000")
    discounted_sales = {
        month : value * 0.9 if value > 18_000 else value
        for month , value in monthly_sales.items()
    }
    print("Discounted sales : " , discounted_sales)
    
    print("Apply taxes of 15 per cent for all months")
    sales_after_tax = {
        month : value * 0.85
        for month , value in monthly_sales.items()
    }
    print("Sales after taxes : " , sales_after_tax)
    
    # total sales
    total_annual_sales = sum(monthly_sales.values()) 
    print("Total sales" , total_annual_sales)
    
    total_annual_sales_2 = reduce(lambda x , y : x + y , monthly_sales.values())
    print("Total sales" , total_annual_sales_2)
    print('-' * 50)
    # best and worst performin month
    best_month =  max(monthly_sales , key=monthly_sales.get) 
    worst_month =  min(monthly_sales , key=monthly_sales.get) 
    
    print(f"Best month  {best_month} with sales {monthly_sales[best_month]}K")
    print(f"Worst month  {best_month} with sales {monthly_sales[worst_month]}K")
    
if __name__ == '__main__':
    main()