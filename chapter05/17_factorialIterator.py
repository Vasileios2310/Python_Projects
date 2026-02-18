class FactoIterator:
    def __init__(self , n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        self.n = n
        self.result = 1 # k!
        self.order = 0 # start from 0 to include 0! , remember which k! counts
        
    def __iter__(self):
        """ returns self , if next() run before for, then for does not start from 0!, but from where iterator has count"""
        return self
    
    def __next__(self):
        if self.order > self.n:
            raise StopIteration
        
        # handle the 0!
        if self.order == 0:
            self.order += 1
            return 1
        
        self.result *= self.order
        self.order += 1
        return self.result
    
def main():
    facto_iterator = FactoIterator(5)
    
    a = next(facto_iterator)
    print(f"0! = {a}")
    
    for facto in facto_iterator:
        print(facto)
        
    print('-' *30)
    
    new_facto_iterator = FactoIterator(5)
    
    for index , factorial in enumerate(new_facto_iterator , start=0):
        print(f"Factorial ({index}) = {factorial}")
    
    

if __name__ == '__main__':
    main()