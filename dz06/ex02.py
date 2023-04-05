# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).

l = int(input('Введите длинну списка: '))
my_list = list(map(int, input().split()[:l]))
print(my_list)

min_=int(input('min--> '))
max_=int(input('max--> '))
for i in range(len(my_list)):
    if min_< my_list[i]<max_:
        print(f'Вывод индексов: {i}')