def minimum(*values , clip = None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

x = minimum(1,2,3,4,-3,-12)
y = minimum(1,2,3,4,-3,-12 , clip=0)

print(x)
print(y)

