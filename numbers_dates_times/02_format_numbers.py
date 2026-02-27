x = 1234.56789
y = 1234567
z = -1234

print('two decimal places accurancy')
print(format(x , '0.2f'))

print('-' * 30)

print('right justified in 10 chars , one-digit accurancy')
print(format(x,'>10.1f'))

print('-' * 30)

print('left justified')
print(format(x,'<10.1f'))

print('-' * 30)

print('centered')
print(format(x,'^10.1f'))

print('-' * 30)

print('inclusion of thousans seperator')
print(format(x,','))
print(format(x,'0,.1f'))

print('-' * 30)

print('binary')
print(format(y,'b'))

print('-' * 30)

print('oct')
print(format(y,'o'))

print('-' * 30)

print('hex')
print(format(z,'x'))