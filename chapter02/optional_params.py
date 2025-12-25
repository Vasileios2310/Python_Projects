def get_date_formatted(day : int= 1, month : int = 1 , year : int = 2000) -> str:
    """_summary_

    Args:
        day (int, optional): _description_. Defaults to 1.
        month (int, optional): _description_. Defaults to 1.
        year (int, optional): _description_. Defaults to 2000.
    """
    return(f"{day:02d}/{month:02d}/{year:04d}")

def main():
    print(get_date_formatted())
    print(get_date_formatted(12,10))
    print(get_date_formatted(14))
    print(get_date_formatted(31,12,2025))
    
    print(get_date_formatted(year=2025 , month=10))

if __name__ == "__main__":
    main()  
    
