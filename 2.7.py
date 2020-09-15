def Day(k):
    day = (365 + 1)%7
    return day

k = input("Введите число в диспазоне 1-365: ")
print(Day(k))
