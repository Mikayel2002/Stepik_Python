# Даны две различные клетки шахматной доски. Напишите программу,
# которая определяет, может ли король попасть с первой клетки на
# вторую одним ходом. Программа получает на вход четыре числа от 1
# до 8 каждое, задающие номер столбца и номер строки сначала для
# первой клетки, потом для второй клетки. Программа должна вывести «YES»,
# если из первой клетки ходом короля можно попасть во вторую, или «NO»
# в противном случае.

a = int(input("Row of first cell: "))
b = int(input("Column of first cell: "))
c = int(input("Row of second cell: "))
d = int(input("Column of second cell: "))

if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
    if -1 <= c - a <= 1 and -1 <= d - b <= 1:
        print("YES")
    else:
        print("NO")
