from typing import List , Tuple , Dict

def get_results(products : List[Tuple[str , int]] , **kwargs) -> List[Tuple[str , int]]:
    """
    Filters a list of products based on given keword arguments.
    Each keyword argument corresponds to a product attribute.
        
    Parameters:
        producs : List[Tuple[str , int]]: A list of tuple , where each tuple contains a brand and a price.
        **kwargs : Arbitrary keyword arguments (brand , price).
            
    Returns:
        List[Tuple[str , int]] : A list of tuples that match the filtering criteria
    """
    results = [
        (brand , price) for brand , price in products if kwargs.get('brand') == brand and kwargs.get('price') == price
    ]
    
    return results



def main():
    products = [("lenovo" , 100) , ("lenovo" , 40) , ("ibm" , 140)]
    criteria = {"brand" : "lenovo" , "price" : 100}
    
    print(get_results(products , **criteria))
        
        
if __name__ == "__main__":
    main()