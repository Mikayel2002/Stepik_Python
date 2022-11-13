# На числовой прямой даны два отрезка: [a1; b1] и [a2; b2].
# Напишите программу, которая находит их пересечение.
# Пересечением двух отрезков может быть:
# отрезок;
# точка;
# пустое множество.

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if min(b1, b2) < max(a1, a2):
    print('пустое множество')
elif min(b1, b2) == max(a1, a2):
    print(min(b1, b2))
else:
    print(max(a1, a2), min(b1, b2))
