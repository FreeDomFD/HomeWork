def func(num):
    if -2.4 <= num <= 5.7:
        return num**2
    else:
        return 4

x = float(input("Введите вещественное число: "))
print("Значение функции: ", func(x))
