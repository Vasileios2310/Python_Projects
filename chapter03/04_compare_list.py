def compare_list(list1 , list2):
    print(f"{list1} is {list2} : {list1 is list2}")
    print(f"{list1} == {list2} : {list1 == list2}")

def main():
    # is --> compares the id from objects
    # == --> compares the value of elements
   
   my_list = [1,2,3]
   your_list = [1,2,3]
   
   print(id(my_list) , id(your_list))
   compare_list(my_list , your_list)
    

if __name__ == "__main__":
    main()