class Collection:
    def __init__(self , data):
        print("init")
        self.data = data
        
    def __iter__(self):
        print("Iter")
        return iter(self.data)
    
    def __len__(self):
        print("len")
        return len(self.data)
    
    def __getitem__(self, index):
        print("get item")
        return self.data[index]
    
    def __repr__(self):
        print("repr")
        return f"DataCollection ({self.data})"
        
def main():
    
    # 1. for item in collection ...
    # 2. unpacking
    # 3. collection[2]
    # 4. collection[1:3]
    # 5. len(collection)
    collection = Collection([1,2,3,4,5])
    
    print(f"Collection {collection}") #  --> def __repr__(self):
    
    print("iteration")
    for item in collection:
        print(item , end=", ")
    print()
    
    print("unpacking")
    print("When unpacking starts, Python calls: Iter and it receives the iterator from self.data (the list)."
          "Then next() pulls values from that list one by one")
    a , b, c, d, e = collection
    
    print(a , b, c, d, e)
    print("indexing")
    print(f"collection[2] : ", collection[2])

    print("slicing")
    print(f"collection[1:3]: {collection[1:3]}")   
    print(f"len collection: {len(collection)}")   
     
    
  
if __name__ == '__main__':
    main()