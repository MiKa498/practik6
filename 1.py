print ("Состояние здоровья")
temp = float(input("Введите температуру"))
presuare = int(input("Введите давление"))
pulse = int(input("Введите пульс"))

if 36<= temp <=37 and 110<= presuare <=130 and 60<= pulse <= 100:
    print ("Нормальное состояние")
elif 35<= temp <36 or 37< temp <=38 and 105<= presuare <110 or  130< presuare <=140 and 55<= pulse <60 or 100< pulse <=110:
    print ("Легкое недомогание")
else:
    print ("Вам нужен врач")