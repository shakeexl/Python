# Новиков Роман
# Задание 4
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

while True:
    number_1 = float(input('Введите действительное положительное число: '))
    number_2 = int(input('Введите целое отрицательное число: '))
    if number_1 <= 0 or number_2 >= 0:
        print('Упс! Числа не соответствуют требованиям. Попробуйте снова')
        continue
    else:
        break


def my_func(x, y):
    k = x
    i = 1
    while i < abs(y):
        x = x * k
        i = i + 1
    return 1 / x


print(my_func(number_1, number_2))