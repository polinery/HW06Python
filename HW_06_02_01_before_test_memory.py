''' Факториал. Тестирование памяти. '''

from memory_profiler import profile


@profile()
def fact_1(n):
    ''' Выводит на экран список из n натуральных чисел и
    соответствующий каждому числу факториал числа без применения
    встроенной функции factorial'''
    factr = 1
    for i in range(1, n + 1):
        print(i, end='! = ')
        factr = factr * i
        return factr


for el in fact_1(int(input('Укажите целое неотрицательное число: '))):
    print(el)