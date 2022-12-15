''' Сотрудники и зарплата. Тестирование по времени. '''

from timeit import timeit

from HW_06_01_02_before import salary_1
from HW_06_01_02_after import salary_2

with open('salary.txt', 'r') as my_file:
    my_list = my_file.read().split('\n')

print(
    f'До: {timeit("salary_1(my_list)", globals=globals(), number=1000)}')
print(
    f'После: {timeit("salary_2(my_list)", globals=globals(), number=1000)}')
