"""Реализовать класс Road (дорога),
в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
асфальтом, толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""

class Road:
    def __init__(self, _length, _width, weight, height):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.height = height

    def count_mass(self):
        road_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Масса асфальта необходимого для покрытия всего дорожного полотна: {road_mass}')

build_road = Road(20, 5000, 25, 5)
build_road.count_mass()
