set_1 = list(map(int, input("Введите первое множество (например - 1, 2, 3, 4, 5, 6, 7): ").split(", ")))
set_2 = list(map(int, input("Введите второе множество (например - 1, 2, 3, 4): ").split(", ")))

print(set_1)
print(set_2)

if set_1 > set_2:
    print(True)
else:
    print(False)