# Новиков Роман
# Задание 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

f = open('test_5.txt', 'w')
numbers = input('Вводите числа через пробел: ').split(' ')
for i in numbers:
    f.writelines(i + ' ')
f.close()

with open('test_5.txt', 'r') as f_2:
    new_numbers = f_2.readline().split()
    print(sum(map(int, new_numbers)))
f_2.close()

