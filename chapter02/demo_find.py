import string

def find(mystring , mycharacter):
    if mycharacter in mystring:
        return mycharacter
    else:
        return -1
    
x = find('Hello World' , 'l')
print(f"The character is {x}")


s = 'hello_3'
s1 = 'Tom and Jerry'
s2 = 'banana'
s3 = 'APPLE'
s4 = '   MANgo   '
s5 = '----Hello---'

print(s.isalpha())
print(s.isdigit() , s.islower())
print(s.startswith('h') , s.endswith('3'))
print(not s.isdigit())

print(s1.find('an'))

print(s1.rfind('rry'))


print(s2.count('na'))

print(s2.capitalize())
print(s2.upper())
print(s3.lower())
print(s4.swapcase())

print(s5.strip('-'))
print(s5.lstrip('-'))
print(s5.rstrip('-'))
print(s4.strip(' '))