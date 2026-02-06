print("рулетка")
number = int(input("Введите номер ячейки рулетки:"))

if 0 <= number <= 36 and 1 < number <= 10 or 19 <= number <= 28 and number % 2 == 0:
    print("Черный цвет")
elif 0 <= number <= 36 and 1<=number<=10 or 19<=number<=28 and number % 2 == 1:
    print("Красный цвет")
elif 0 <= number <= 36 and 11<=number<=18 or 29<=number<=36 and number % 2 == 1:
    print("Черный цвет")
elif 0<=number <= 36 and 11<=number<=18 or 29<=number<=36 and number % 2 == 0:
    print("Красный цвет")
elif number == 0:
    print("Зеленый карман")
else:
    print("Ошибка ввода")
