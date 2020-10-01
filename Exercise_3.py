# Новиков Роман
# Задание 3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))


def my_func(a, b, c):
    my_list = [a, b, c]
    i = my_list.index(max(my_list))
    m = my_list[i]
    my_list.pop(i)
    k = my_list.index(max(my_list))
    n = my_list[k]
    print('Сумма наибольших аргументов равна', m + n)


my_func(number_1, number_2, number_3)
