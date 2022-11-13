# Напишите программу, которая считывает три числа и подсчитывает сумму
# только положительных чисел.

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
s = 0

if a > 0:
    s += a
if b > 0:
    s += b
if c > 0:
    s += c

print(s)
