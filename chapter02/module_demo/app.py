#import my_calculation
from my_calculation import my_add  as my_add_function, num1

num2 = 36

#res = my_calculation.my_add(num2 , my_calculation.num1)
# res = my_add(num1 , num2)
res = my_add_function(num1 , num2)


print(res)
print(__name__)