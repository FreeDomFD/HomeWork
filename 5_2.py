def max_num(num1, num2):
    """Определяет максимальное из двух введенных чисел"""
    if num1 > num2:
        return num1
    else: return num2

number1, number2 = map(int, input("Введите 2 целых числа через пробел: ").split())
print("Наибольшее число: ", max_num(number1, number2))
        
