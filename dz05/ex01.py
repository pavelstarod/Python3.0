# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
def step(a, b):
    if b > 1:
        res = a*step(a, b-1)
        return res
    elif b == 1:
        return a


a = int(input('a--> '))
b = int(input('b--> '))
print(step(a, b))
