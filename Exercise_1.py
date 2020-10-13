# Новиков Роман
# Задание 1
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
import time


class TrafficLight:
    def __init__(self):
        self._colors = cycle(['Красный', 'Желтый', 'Зеленый'])

    def running(self):
        for color in self._colors:
            if color == 'Красный':
                print(color)
                time.sleep(7)
            elif color == 'Желтый':
                print(color)
                time.sleep(2)
            else:
                print(color)
                time.sleep(5)


my_trafficlight = TrafficLight()
my_trafficlight.running()