mySet = list(map(int, input("Введите список чисел (например - 1, 2, 3, 2, 1, 1): ").split(", ")))
myObject = set()

for i in range(len(mySet)):
    myObject.add(mySet[i])

print(myObject)
print(len(myObject))