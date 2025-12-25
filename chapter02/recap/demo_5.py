a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = 0
d = 0

for i in range(len(a)):
    c += a[i]*b[i]
print(c)

print('------------SECOND WAY-----------')

C = []
for i,j in zip(a,b):
    C.append(i*j)
print(C)
d = sum(C)
print(d)