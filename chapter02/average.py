def get_average(*num):
    """_summary_

    Returns:
        _type_: _description_
    """
    if not num:
        return "No num provided"
        
    average = sum(num) / len(num)
    return average

def main():
    
    numbers = [12,14,55]
    
    average = get_average(*numbers)
    print(get_average(average))


if __name__ == "__main__":
    main()