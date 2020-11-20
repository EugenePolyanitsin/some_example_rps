from functools import reduce

def my_list(el1, el2):
    return  el1 * el2

sec_list = [el for el in range(100, 1001, 2)]
print(f"Список\n{sec_list}\nРезультат произведения элементов\n{reduce(my_list, sec_list)}")
