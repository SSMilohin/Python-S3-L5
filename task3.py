n, citiesList = int(input("Количество городов: ")), set()

for i in range(n):
    city = input()
    citiesList.add(city)

currentCity = input("Какой город нужно проверить на наличие: ")

if currentCity in citiesList:
    print("REPEAT")
else:
    print("OK")