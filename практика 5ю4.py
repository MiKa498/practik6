import math
print("*** Калькулятор площади ***")
def calculate_rectangle_area(width, height): #Вычисляет площадь прямоугольника
    return width * height
def calculate_circle_area(radius): #Вычисляет площадь круга
    return 2 * math.pi * radius
width = float(input("Введите ширину прямоугольника:"))
height = float(input("Введите высоту прямоугольника:"))
radius = float(input("Введите радиус окружности:"))
print(f"Площадь прямоугольника равна: {calculate_rectangle_area(width, height):.2f}")
print(f"Площадь окружности равна: {calculate_circle_area(radius):.2f}")