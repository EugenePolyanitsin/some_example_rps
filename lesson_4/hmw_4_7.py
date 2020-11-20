
def fact_gen(n):
    f_num = 1
    for el in range(1, n + 1):
        f_num *= el
        yield f_num

for el in fact_gen(5):
    print(el)

