def func(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s

if __name__ == "__main__":
    new_s = str(input("Введите строку: "))
    new_n = int(input("Введите число: "))
    print(func(new_s, new_n))
