# Новиков Роман
# Задание 2
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, parameter):
        self.parameter = parameter

    @property
    def consumption(self):
        result = (self.parameter / 6.5) + 0.5
        return round(result, 2)


class Suit(Clothes):
    def __init__(self, parameter):
        self.parameter = parameter

    @property
    def consumption(self):
        result = (2 * self.parameter) + 0.3
        return round(result, 2)


my_coat = Coat(54.1234)
print(my_coat.consumption)

my_suit = Suit(175.96)
print(my_suit.consumption)

print('Общий расход:', my_coat.consumption + my_suit.consumption)