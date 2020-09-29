import random
def game():
    """Запуск игры"""
    num1 = random.randint(1, 10)
    num2 = int(input("Введите число от 1 до 10: "))
    if num2 != num1:
        print("Повторите еще раз")
    else:
        print("Победа")

if __name__ == "__main__":
    game()
