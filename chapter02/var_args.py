def print_cities(*cities):
    """_summary_
    
    """
    if not cities:
        print("No cities provided")
    else:
        print("Cities: " , " , " .join(cities))
        
def main():
    print_cities("Athens" , "Patra" , "Tripoli")
    
if __name__ == "__main__":
    main()
    