from datetime import datetime, timedelta
   
    
def main():
    print("1. Current date and time")
    now = datetime.now()
    print(f"Curent date and time {now}")
    print(f"European format : {now.strftime('%d/%m/%Y %H:%M:%S')}")
    
    print("Create specific datetime")
    specific_date_time = datetime(2026 , 2 , 8 , 15 , 30)
    print(f"Specific date time : {specific_date_time.strftime('%d/%m/%Y %H:%M')}")
    
    european_date_str = "08/02/2026 15:30"
    parsed_date = datetime.strptime(european_date_str , '%d/%m/%Y %H:%M')
    
    print("\nDate arithmetic")
    one_week_later = parsed_date + timedelta(weeks=1)
    print(f"One week later : {one_week_later.strftime('%d/%m/%Y %H:%M')}")    
    
    print("\nComparing Dates")
    today = datetime.now()
    if parsed_date > today:
        print(f"{parsed_date.strftime('%d/%m/%Y %H:%M')} is in the future")
    elif parsed_date < today:
        print(f"{parsed_date.strftime('%d/%m/%Y %H:%M')} is in the past")
    else:
        print(f"{parsed_date.strftime('%d/%m/%Y %H:%M')} is now")
        
    try:
        from babel.dates import format_datetime
        
        print("\nLocalized datetime")
        print(format_datetime(now , format='full' , locale='it_IT'))
    except ImportError:
        print("Babel not installed")
        
if __name__ == "__main__":
    main()