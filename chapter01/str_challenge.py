message = "Factory"

for i in range(len(message)):
    print(message[i] * (i + 1))
print()

for i in range(len(message)):
    print(message[i] * (i + 1) , end= "*" * (len(message) - 1 - i) )
    print()
