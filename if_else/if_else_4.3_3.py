# Даны три различных целых числа. Напишите программу,
# которая находит среднее по величине число.

a, b, c = int(input()), int(input()), int(input())

if a < b:
    # x = b
    if b < c:
        print(b)
    else:
        # m = c
        if a < c:
            print(c)
        else:
            print(a)
else:
    # x = a
    if a > c:
        # m = c
        if c < b:
            print(b)
        else:
            print(c)
    else:
        print(a)
