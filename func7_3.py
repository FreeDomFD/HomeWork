import math
def sqrt_func(x):
    """Вычисление выражения по введенному значению"""
    return (math.sqrt(1-(math.sin(x)**2)))

if __name__ == "__main__":
    num = float(input("Введите x: "))
    print(math.sqrt(1 - (math.sin(num)**2)))
