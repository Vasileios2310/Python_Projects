def print_cities(*cities, separator = ", " , end= "\t"):
    """_summary_

    Args:
        separator (str, optional): _description_. Defaults to ", ".
        end (str, optional): _description_. Defaults to "\t".
    """
    if not cities:
        print("No cities provided")
    else:
        print("Cities: " , " , " .join(cities) , sep=separator , end=end)
        
def main():
    print_cities("Athens" , "Patra" , "Tripoli" , separator=" | " , end=" . ")
    
if __name__ == "__main__":
    main()
    