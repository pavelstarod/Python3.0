# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input('Введите N: '))
A = list(map(int, input().split()[:N]))
X = int(input('Введите X: '))
result = 0
for i in range(len(A)):
    if X-A[i] < X-result and X-A[i] > 0:
        result = A[i]
print(result)
