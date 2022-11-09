# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.

import random

numbers = [random.randint(0, 9) for i in range(15)]
print()

numb1 = "".join(map(str, numbers))
print(numb1)
print()

n = str(input("Введите трехзначное натуральное число: "))
print()
numb2 = "".join(map(str, n))

count = 0
for i in range(len(numb1)):
    if numb2 == numb1[i:i+len(numb2)]:
        count += 1

print(f"Число {n} в массиве встречается {count} раз")