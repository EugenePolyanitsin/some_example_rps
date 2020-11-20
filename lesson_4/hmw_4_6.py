from itertools import count
print("Нажмите Enter для генерации числа. Нажмите q чтобы выйти")
for el in count(int(input('Введите стартовое число: '))):
    print(el, end="")
    quit = input()
    if quit  == "q":
        break
from itertools import cycle
print("Нажмите Enter для генерации повтора. Нажмите q чтобы выйти")

my_list = input("Введите спсиок разделяя элементы пробелом: ").split()
n = cycle(my_list)
quit = None

while quit != "q":
    print(next(n), end="")
    quit = input()



