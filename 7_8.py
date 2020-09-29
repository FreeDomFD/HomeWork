import random
def kubik():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print("Бросает первый игрок:", a)
    print("Бросает второй игрок:", b)
    if a > b:
        print("Победил первый игрок!")
    else:
        print("Победил второй игрок!")
kubik()
