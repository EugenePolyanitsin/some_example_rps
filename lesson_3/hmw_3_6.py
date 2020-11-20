def int_func(a):
    return a.title()


print(int_func("леха"))

def my_func(a):
    s_word = a.split(' ')
    total = []
    for i in s_word:
        str_element = str(i)
        first = int_func(str_element)
        total.append(first)
    return total


print(my_func("hello world or not"))
