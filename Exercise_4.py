# Новиков Роман
# Задание 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f = 'test_4.txt'

f_obj = open(f)

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []

for i in f_obj:
    i = i.split(' ', 1)
    my_list.append(translate[i[0]] + ' ' + i[1])

f_obj.close()

f_2 = open('test_4_2.txt', 'w')
for i in my_list:
    f_2.writelines(i)
f_2.close()

with open('test_4_2.txt', 'r') as f_2:
    print(f_2.read())
f_2.close()




