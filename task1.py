# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите число n "))
m = int(input("Введите число m "))
i=1
j=1
list1 =list()
list2 =list()
while i<n+1:
    list1.append(input(f"Введите {i} число"))
    i+=1
while j<n+1:
    list2.append(input(f"Введите {j} число"))
    j+=1

my_set1 = set(list1)
my_set2 = set(list2)
c = sorted(my_set1.intersection(my_set2))
print(c)




# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)