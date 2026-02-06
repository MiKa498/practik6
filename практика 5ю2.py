parameters = input("Введите свой вес (в 'кг') и рост (в 'м') через пробел:").split()
weight, height = map(float, parameters)
IMT = weight / (height * height)
print(f"Ваш ИМТ: {IMT:.1f}")
