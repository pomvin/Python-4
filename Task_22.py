"""Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго 
множества. Затем пользователь вводит сами элементы множеств."""

n = int(input("Введите кол-во элементов первого множества: "))
set1 = set([int(i) for i in input(f"Введите {n} элементов первого множества: ").split()])

m = int(input("Введите кол-во элементов второго множества: "))
set2 = set([int(i) for i in input(f"ведите {m} элементов второго множества: ").split()])

set3 = set1.intersection(set2)
to_list = list(set3)
to_list.sort()

print(*set3)

