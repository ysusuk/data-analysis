blah = 'blah'
blahs = [1, 2, 'three', 4.0, blah]
# blahs = ['1', '2', '3']
print(blahs)
print(blahs[2])
print(str(blahs[1]).title())
blahs[2] = 3
print(blahs)
blahs.append(6)
print(blahs)
blahs.insert(4, 5)
print(blahs)
del blahs[5]
print(blahs)
print('length ' + str(len(blahs)))
first = blahs.pop(0)
last = blahs.pop()
print(first)
print(last)
print(blahs)
blahs.remove(4.0)
print(blahs)
blahs.append(1)
blahs.append(4)
blahs.sort(reverse = True)
print(blahs)
blahs.reverse()
print(blahs)

for blah in blahs:
    print(blah)
print("one blah in a line")

for num in range(2, 10, 2):
    print(num)
print("even blahs")

squares = []
for value in range(1, 11):
    squares.append(value**2)
print("squares: " + str(squares))

squares = [value**2 for value in range(1,11)]
print("for comprehension squares: " + str(squares))

print(min(squares))
print(max(squares))
print(sum(squares))


print(blahs[0:3])

print(blahs[:2])
print(blahs[-2:])
print(blahs[3:])
print(blahs[:-2])

print(blahs[:])
dimension = (1, 2)
print(dimension[0])
print(dimension[1])

