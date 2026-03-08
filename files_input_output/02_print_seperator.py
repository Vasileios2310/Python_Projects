print('Python' , 'hello' , 15 , [0,1] , sep='-')

print('Python' , 'hello' , 15 , [0,1] , sep='//' , end='!!\n')


for i in range(5):
    print(i , end='\n')
    
print('-' *30)

data = ('Python' , 'hello' , 15 , [0,1])

print(',' .join(str(d) for d in data))
print('-' *30)
print(*data , sep=',')
