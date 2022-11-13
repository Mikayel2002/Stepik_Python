# Напишите программу, которая определяет наименьшее из четырёх чисел.

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))

if a < b:
    minimum = a
else:
    minimum = b

if c < d:
    minimum_1 = c
else:
    minimum_1 = d

if minimum < minimum_1:
    print(minimum)
else:
    print(minimum_1)
