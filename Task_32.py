# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е.
# не меньше заданного минимума и не больше заданного максимума)
import random

myList = [random.randint(0, 20) for i in range(random.randint(10, 20))]
print(myList)
result = list()

max = int(input("Максимум: "))
min = int(input("Минимум: "))

for i in range(len(myList)):
    if min <= myList[i] <= max:
        result.append(i)

print(result)