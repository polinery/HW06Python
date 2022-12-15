''' Сотрудники и зарплата. Тестирование памяти.'''

from memory_profiler import profile


@profile()
def salary_1(lst):
    sal = []
    poor = []
    for i in lst:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
    return [poor, sal]


with open('salary.txt', 'r') as my_file:
    my_list = my_file.read().split('\n')
print(
    f'Оклад меньше 20000 у: {salary_1(my_list)[0]}, \n'
    f'Cредний оклад {sum(map(int, salary_1(my_list)[1])) / len((salary_1(my_list)[1]))}')
