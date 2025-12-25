def inc_first(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    list[0] = list[0] + 1
    print(list)
    
    
a = [3]
inc_first(a)
print(a)

print("---------------")

def g(x):
    x = x + 1

b = 3
g(b)
print(b)     # 3  ← not changed
