'# импорт функции sqrt из модуля MATH'
from math import sqrt

a = int(input('Введите "a"= '))
b = int(input('Введите "b"= '))
c = int(input('Введите "c"= '))

d = b ** 2 - 4 * a * c

if d < 0:
    print('Решения нет')
elif d == 0:
    x = -b / (2 * a)
    print('Решение x =', x)
else:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print('Ршения два')
    print('x1 =', x1)
    print('x2 =', x2)
