def bmi(mass, height):
    """Вычисляет индекс массы тела по массе и росту человека"""
    return mass/((height/100)**2)

p_mass, p_height = map(float,input("Введите свой вес(кг) и рост(см) через пробел: ").split())
BMI = bmi(p_mass, p_height)

if BMI < 18.5:
    print("Ниже нормального веса")
elif 18.5 <= BMI < 25:
    print("Нормальный вес")
elif 25 <= BMI < 30:
    print("Избыточный вес")
elif 30 <= BMI < 35:
    print("Ожирение первой степени")
elif 35 <= BMI < 40:
    print("Ожирение второй степени")
elif BMI >= 40:
    print("Ожирение третьей степени")
