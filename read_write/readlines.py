f = open('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt', 'w')
f.write('first line\nSecond line\nThird line')

f.close()

f = open('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt', 'r')
line = f.readline()
print(line)

lines = f.readlines()
print(lines)

