# Новиков Роман
# Задание 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите значение числа n: ')
n_1 = n
n_2 = n + n
n_3 = n + n + n
result = int(n_1) + int(n_2) + int(n_3)
print('Ответ равен:', result)

