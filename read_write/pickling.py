import pickle

f = open('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt', 'wb')
pickle.dump(3.14 , f)
pickle.dump([1,2,3] , f)
f.close()

f = open('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt', 'rb')
x = pickle.load(f)
print(x)

l = pickle.load(f)
print(l)

f.close()