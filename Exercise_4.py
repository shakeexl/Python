# Новиков Роман
# Задание 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))

remainder = number % 10
number = number // 10
while number > 0:
    if number % 10 > remainder:
        remainder = number % 10
    number = number // 10
print(remainder)
