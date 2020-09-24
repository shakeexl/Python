# Новиков Роман
# Задание 2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds_amount = input('Введите количество секунд: ')
hours = int(seconds_amount) // 3600
minutes = (int(seconds_amount)-(3600*hours)) // 60
seconds = int(seconds_amount)-((3600*hours)+(60*minutes))
print(f'Время: {hours}:{minutes}:{seconds}')
