# Новиков Роман
# Задание 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, car_color, car_speed, car_name, car_is_police):
        self.color = car_color
        self.speed = car_speed
        self.name = car_name
        self.is_police = car_is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости! Скорость автомобиля равна', self.speed)
        else:
            print('Скорость автомобиля равна', self.speed)


class SportCar(Car):
    def show_speed(self):
        print('Скорость автомобиля равна', self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости! Скорость автомобиля равна', self.speed)
        else:
            print('Скорость автомобиля равна', self.speed)


class PoliceCar(Car):
    def show_speed(self):
        print('Скорость автомобиля равна', self.speed)


my_workcar = WorkCar('Желтый', 60, 'Трактор', False)
my_workcar.go()
my_workcar.show_speed()
print(my_workcar.is_police)