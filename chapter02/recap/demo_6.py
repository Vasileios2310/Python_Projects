def list_2_3_not5():
    L = []
    for x in range (1, 101):
        if x % 2 == 0 and x % 3 == 0 and x % 5 != 0:
            L.append(x)
    return L

new_list = list_2_3_not5()
print(new_list)
print(new_list[0])