# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март',
                4: 'Апрель', 5: 'Май', 6: 'Июнь',
                7: 'Июль', 8: 'Август', 9: 'Сентябрь',
                10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
month = int(input("Введите номер месяца от 1 до 12: "))
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(month))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(month))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(month))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(month))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")
