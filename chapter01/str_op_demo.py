message = "Coding Factory"
 
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

print(f"Number of characters for message : {message} {len(message)}")

for char in message:
    print(char , end=" ")
print()

for i in range(10):
    print(i , end=" ")
print()

for j in range(len(message)):
    print(message[j] , end = " ")
print()

for num in range(1,10,2):
    print(num , end=" ")
print()