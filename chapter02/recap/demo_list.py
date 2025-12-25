def pos_neg_list(L):
    """_summary_

    Args:
        L (_type_): _description_

    Returns:
        _type_: _description_
    """
    Positive = []
    Negative = []
    count_zero = 0
    
    for i in L:
        if i > 0 :
            Positive.append(i)
        if i < 0 :
            Negative.append(i)
        if i == 0:
            count_zero += 1
    return Positive , Negative , count_zero  

x = pos_neg_list([0, -1, 2 , -1 , 2 , 0 , -77 , 0])
print(f"List with positive is : {x[0]}")
print(f"List with negative is : {x[1]}")
print(f"Count zero is : {x[2]}")

print("--------List of list--------")

def list_to_list(name,surname,age):
    if not(len(name) == len(surname) == len(age)):
        return 'error'
    else:
        Person = []
        for n , s , a in zip(name , surname , age):
            Person.append([n , s , a])
        return Person
    
x = list_to_list(['bill'] , ['krit'] , [35])
print(x)