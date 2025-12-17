print ("Цвета колеса рулетки")
number = int(input("Введите число"))
if number < 37:
    if number == 0:
        print ("Зеленый цвет")
    elif 1<= number <=10 or 19<= number <=28  | number %2 == 0:
            print ("Черный цвет")
    elif 11<= number <=18 or 29<= number <=36 | number %2 != 0:
        print ("Черный цвет")
    elif 1<= number <=10 or 29 <= number <=36 | number %2 == 0:
        print ("Красный цвет")
    elif 1<= number <=10 or 19 <= number <=28 | number %2 != 0:
        print ("Красный цвет")
else:
    print("Некорректное число")
