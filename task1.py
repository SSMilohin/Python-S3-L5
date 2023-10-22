myList = list(map(int, input("Введите список чисел (например - 1, 2, 3, 2, 1, 1): ").split(", ")))
mySet = set()

for i in range(len(myList)):
    mySet.add(myList[i])

print(mySet)
print(len(mySet))