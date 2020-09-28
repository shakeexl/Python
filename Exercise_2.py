# Новиков Роман
# Задание 2
# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []

i = 0
while len(my_list) < 7:  # Ограничение количества элементов листа
    user_input = int(input('Введите какое-нибудь число: '))
    my_list.insert(i, user_input)
    i = i + 1
my_new_list = my_list

print(my_list)

k = 0
if len(my_list) % 2 == 0:
    while k < (len(my_list)-1):
        my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]
        k = k + 2
elif len(my_list) % 2 != 0:
    while k < (len(my_list)-2):
        my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]
        k = k + 2

print(my_list)