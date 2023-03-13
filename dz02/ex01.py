# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите кол-во монеток: '))
coins = []
for i in range(n):
    peso = int(input('Введите орел(1) или решка(0): '))
    coins.append(peso)
orel = 0
reshka = 0
for item in coins:
    if item == 1:
        orel += 1
    elif item == 0:
        reshka += 1
if orel > reshka:
    print(reshka)
else:
    print(orel)
