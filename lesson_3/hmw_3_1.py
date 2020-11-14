def my_func(a, b):
    try:
        a = int(input("Input dividend: "))
        b = int(input("Input divider: "))
        res = a / b
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"
    return res


print(f'result  {my_func()}')
