from sys import  argv

def my_func(time, rate, bonus):
    try:
        return time * rate + bonus
    except ValueError as err:
        print("Error: ", err)


print(f"Calculation - {my_func(*map(float, argv[1:]))}")


