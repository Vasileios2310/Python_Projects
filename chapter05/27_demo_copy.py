import copy
"""
when you do a shallow copy ([:], .copy(), list()), 
Python creates a new outer list, but the inner objects are still shared.
Integers are immutable → reassignment (ages[0] = 100) affects only that list reference

Lists are mutable → changing nested list contents (ages[1][0] = 200) affects all shallow copies that share it
"""


def main():
    ages = [ 10 , [ 20 , 30 , 40 ] , 50 ]
    
    # methods to create copies
    # shallow copy
    age_slice = ages[:]
    ages_cp = ages.copy()
    ages_list = list(ages)
    
    # deep copy
    ages_dcp = copy.deepcopy(ages)
    
    print("Original list:" , ages)
    print("Slicing ages:" , age_slice)
    print("List() ages:" , ages_list)
    print("deep copy:" , ages_dcp)
    
    # modify the original list
    ages[0] = 100
    ages[1][0] = 200
    
    print("After modification:")
    print("Original list:" , ages)
    print("Slicing ages:" , age_slice)
    print("List() ages:" , ages_list)
    print("deep copy:" , ages_dcp)
    
if __name__ == "__main__":
    main()   
        