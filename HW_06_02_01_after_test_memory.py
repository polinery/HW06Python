''' Факториал. Тестирование памяти. '''

from memory_profiler import profile
from math import factorial


@profile()
def fact_2(n):
    ''' Выводит на экран список из n натуральных чисел и
        соответствующий каждому числу факториал числа, вычисленный с применением
        встроенной функции factorial'''
    for i in range(1, n + 1):
        print(i, end='! = ')
        return factorial(i)


for el in fact_2(int(input('Укажите целое неотрицательное число: '))):
    print(el)
