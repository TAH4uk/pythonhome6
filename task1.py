# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN

n = int(input("Введите число : "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", comp)