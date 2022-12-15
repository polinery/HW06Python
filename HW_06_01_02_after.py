''' Сотрудники и зарплата. Заменено формирование списков функцией .append
на списковвое включение'''


def salary_2(lst):
    lst = [i.split() for i in lst]
    poor = [i[0] for i in lst if int(i[1]) < 20000]
    sal = [int(i[1]) for i in lst]
    return [poor, sal]


with open('salary.txt', 'r') as my_file:
    my_list = my_file.read().split('\n')
print(
    f'Оклад меньше 20000 у: {salary_2(my_list)[0]}, \n'
    f'Cредний оклад {sum(map(int, salary_2(my_list)[1])) / len((salary_2(my_list)[1]))}')
