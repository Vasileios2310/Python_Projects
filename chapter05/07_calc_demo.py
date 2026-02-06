import functools


def calculate(args):
    def plus():
        return functools.reduce(lambda x , y : x + y , args )
        
    def minus():
        return functools.reduce(lambda x , y : x - y , args , 0) # --> -15
        # return functools.reduce(lambda x , y : x + y , args) --> -13
        
    def mul():
        return functools.reduce(lambda x , y : x * y , args)
        
    def div():
        if sum(args[1:]) != 0:
            return args[0] / sum(args[1:])
        
    return plus , minus , mul , div

def main():
    my_range = range(1,6)
    my_list = list(my_range)
    
    add_func , minus_func , mul_func , div_func = calculate(my_list)
    
    print("add_func"  , add_func())
    print("minus_func"  , minus_func())
    print("mul_func"  , mul_func())
    print("div_func"  , div_func())
    
if __name__ == '__main__':
    main()