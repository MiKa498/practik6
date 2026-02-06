import math
print("Вычисление площади фигур")

def calculate_rectangle_area(width, height):
    """
    Вычисляет и возвращает площадь прямоугольника.

    Args:
        width (float): ширина прямоугольника.
        height (float): высота прямоугольника.

    Returns:
        float: площадь прямоугольника (width * height).
    """
    return width * height

def calculate_circle_area(radius):
    """
    Вычисляет и возвращает площадь круга.

    Args:
        radius (float): радиус круга.

    Returns:
        float: площадь круга (π * radius^2).
    """
    return math.pi * radius ** 2

# Прямоугольник
width, height = map(float, input("Введите ширину и высоту прямоугольника через пробел: ").split())

rectangle_area = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника: {rectangle_area:.2f}")

# Круг
radius = float(input("Введите радиус круга: "))

circle_area = calculate_circle_area(radius)
print(f"Площадь круга: {circle_area:.2f}")