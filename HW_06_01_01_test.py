''' Факториал. Тестирование по времени. '''

from timeit import timeit

from HW_06_01_01_before import fact_1
from HW_06_01_01_after import fact_2

print(
    f'Без встроенной функции: {timeit("fact_1(10)", globals=globals(), number=1000)}')
print(
    f'Со встроенной функцией: {timeit("fact_2(10)", globals=globals(), number=1000)}')
