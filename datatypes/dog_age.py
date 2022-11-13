# На вход программе подается число nn – количество собачьих лет. 
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.

dog_age = int(input("Dog age: "))
human_age = 0

if dog_age <= 2:
    human_age += dog_age * 10.5
else:
    human_age += 21 + (dog_age - 2) * 4

print(human_age)
