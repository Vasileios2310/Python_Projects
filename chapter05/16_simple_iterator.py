class SimpleIterator:
    def __init__(self , data):
        self.data = data    # attribute data references in the same list with numbers = [10 , 20 , 30 , 40 , 50]
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
def main():
    numbers = [10 , 20 , 30 , 40 , 50]
    
    my_iterator = SimpleIterator(numbers)
    
    
    # -> next(my_iterator) <-
    
    for number in my_iterator:
        print(number)
    
    
if __name__ == '__main__':
    main()