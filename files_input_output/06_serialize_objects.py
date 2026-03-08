import pickle

f = open('somefile' , 'wb')
pickle.dump([1,2,3,4] , f)
pickle.dump('hello' , f)
pickle.dump({'Apple ' , 'Banana' , 'Pear'} , f)

f.close()

f = open('somefile' , 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))