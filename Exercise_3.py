# Новиков Роман
# Задание 3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, workers_name, workers_surname, workers_position, wage, bonus):
        self.name = workers_name
        self.surname = workers_surname
        self.position = workers_position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print('Сотрудник:', self.name + ' ' + self.surname)

    def get_total_income(self):
        print('Полный доход:', int(self._income['wage'])+ int(self._income['bonus']))


my_position = Position('Roman', 'Novikov', 'programmer', 172500, 20000)
my_position.get_full_name()
my_position.get_total_income()