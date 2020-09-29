import math
def func(num):
    if 0.2 <= num <= 0.9:
        return math.sin(num)
    else:
        return 1
x = float(input("Введите любое вещественное число: "))
print(func(x))
    
