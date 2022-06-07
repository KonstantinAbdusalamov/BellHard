from abc import abstractmethod
import math

class Car:
    __brand = 'Toyota'
    __model = 'Yaris'
    __year = 2015
    __speed = 0

    def engine(self):
        print('Двигатель заведен')

    def speed_up(self):
        Car.speed = 0
        up = Car.speed
        up = up + 5
        return f'Нажали на газ, скорость {up}'

    def speed_down(self):
        Car.speed = 0
        down = Car.speed
        down = down - 5
        return  f'Нажали на газ, скорость {down}'

    def reverse(self):
        Car.speed = 0
        speed_reverse = Car.speed * -1
        return f'Нажали на разворот, скорость {speed_reverse}'


car_a = Car()
print(car_a.speed_up())
print(car_a.speed_down())
print(car_a.reverse())
