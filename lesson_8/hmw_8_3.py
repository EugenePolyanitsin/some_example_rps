class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите числа для наполнения списка: '))
                    ex = input(f'"{user_val}" Добавленно в список.\n Нажмите Enter для продолжения или введите stop чтобы вывести список: ').lower()
                    self.my_list.append(user_val)
                    if ex == 'stop':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Вы ввели не число! Введите число или введите stop: ").lower()
                if ex == 'stop':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()