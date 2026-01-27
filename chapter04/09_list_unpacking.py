my_list = [1 , 2 , 3 , 4 , 5]

# simple unpacking
a , b , c , d , e = my_list
print(f"Unpack all values --> a = {a} , b = {b} , c = {c} , d = {d} , e = {e}")

# ignore 2nd and 4th value
a1 , _ , c1 , _ , e1 = my_list
print(f"Unpack values ignoring some --> a = {a1} , c = {c1} , e = {e1}")

# unpackint the first element and capturing the rest in a list
a2 , *rest = my_list
print(f"First element  a2 = {a2} , Remaining elements : rest {rest}")

# unpackint the last element and capturing the rest in a list
*start , a3 = my_list
print(f"First elements : start {start} , Last element is a3 = {a3} ")

# unpacking first and last element and the rest
start , *middle , last = my_list
print(f"First element : {start} , middle elements {middle} and last element {last} ")


try:
    a , b , c , e = my_list
    print(f"Unpack all values --> a = {a} , b = {b} , c = {c} , d = {d} , e = {e}")
except ValueError as ve:
    print("Error" , ve)
    
#unpackinf 1st and 2nd element and rest in a list
start , second, *rest  = my_list
print(f"First element : {start} , second element {second} , rest {rest} ")