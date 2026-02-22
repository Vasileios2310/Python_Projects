def main():
    store_a_products = {"Apples" , "Bananas" , "Cherries" , "Elderberries"}
    store_b_products = {"Bananas" , "Cherries" ,"Figs" , "Grapes"}
    
    print("Original store a: " , store_a_products)
    print("Original store b: " , store_b_products)
    
    # intersection
    common_products = store_a_products.intersection(store_b_products)
    # common_products = store_a_products  & store_b_products
    print("Common products : " , common_products)
    
    # union
    all_products = store_a_products  | store_b_products
    # all_products = store_a_products.union(store_b_products)
    print("All products : " , all_products)
    
    # products in a but not in b
    products_in_a_not_b = store_a_products  - store_b_products
    print("Products in a but not in b : " , products_in_a_not_b)
    
    # symmetric difference
    unique_either_products = store_a_products ^ store_b_products
    print("Products in a or in b but not in (A and B) : " ,unique_either_products)
    
if __name__ == "__main__":
    main()   
        