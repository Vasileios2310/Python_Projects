fname = input('Give the file name : ')

try:
    file = open(fname , 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print('File not found' , fname)
    