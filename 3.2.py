def work(a,b,c):
    su = a + b + c
    pr = a * b * c
    return su, pr
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
su, pr = work(a,b,c)
print("Сумма введенных чисел: ", su)
print("Произведение введеных чисел: ", pr)
