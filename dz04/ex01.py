# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите n: '))
m = int(input('Введите m: '))
n_list = set(map(int, input().split()[:n]))
m_list = set(map(int, input().split()[:m]))
all_set = n_list.union(m_list)
all_set2 = all_set.copy()
result = []
for i in all_set:
    min_ = min(all_set2)
    result.append(min_)
    all_set2.remove(min_)
print(result)
