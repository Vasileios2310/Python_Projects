f = open('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt', 'w')
line1 = 'this is first line \n'
f.write(line1)

line2 = 'this is second line \n'
f.write(line2)

f.write(str([2,4,6,8]))

f.close()