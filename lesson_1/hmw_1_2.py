# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

tm = int(input("Введите время в секундах "))
h = tm // 3600
m = (tm - h * 3600) // 60
s = tm - (h * 3600 + m * 60)
print("Время в формате 'чч:мм:сс' %02d:%02d:%02d" % (h, m, s))