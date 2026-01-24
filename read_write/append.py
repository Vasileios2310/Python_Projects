f = open('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt', 'a')
f.write('\n extra line')

f.close()

f = open('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt', 'r')
text = f.read()
print(text)