sum_even = []
sum_odd = []

for i in range(1 , 10):
    if i % 2 == 0:
        sum_even.append(i)
    else:
        sum_odd.append(i)

print(f"evens sum : {sum_even}")
print(f"odds sum : {sum_odd}")