from collision.IsCorrectRect import isCorrectRec
from collision.IsCollisionRect import isCollisionRec
from collision.IntersectionAreaRect import intersectionAreaRec
from collision.IntersectionAreaMultiRect import intersectionAreaMultiRec
def main():
    while True:
        # Запрашиваем выбор пользователя
        number = int(input("Выбор: 1 - intersectionAreaRect , 2 - isCorrectRect , 3 - isCollisionRect , 4 - intersectionAreaMultiRect , 5 - Выход: "))

        if number == 1:
            # Пример использования функции для нахождения площади пересечения двух прямоугольников
            print("Введите координаты двух прямоугольников:")
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [((x1, y1), (x2, y2)), ((x3, y3), (x4, y4))]
            area = intersectionAreaRec(rectangles)
            print(f"Площадь пересечения: {area}")

        elif number == 2:
            # Пример использования функции для проверки корректности прямоугольника
            rectangles = []
            print("Введите координаты прямоугольника:")
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            rectangles.append([(x1, y1), (x2, y2)])
            try:
                if isCorrectRec(rectangles):
                    print("Прямоугольник корректен.")
                else:
                    print("Прямоугольник некорректен.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif number == 3:
            # Пример использования функции для проверки столкновения двух прямоугольников
            print("Введите координаты двух прямоугольников:")
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [((x1, y1), (x2, y2)), ((x3, y3), (x4, y4))]
            collision = isCollisionRec(rectangles)
            if collision:
                print("Прямоугольники пересекаются.")
            else:
                print("Прямоугольники не пересекаются.")

        elif number == 4:
            # Пример использования функции для нахождения площади пересечения множества прямоугольников
            n = int(input("Количество прямоугольников: "))
            rectangles = []
            for i in range(n):
                print(f"Прямоугольник {i + 1}:")
                x1 = float(input('Введите x1: '))
                y1 = float(input('Введите y1: '))
                x2 = float(input('Введите x2: '))
                y2 = float(input('Введите y2: '))
                rectangles.append([(x1, y1), (x2, y2)])
            
            try:
                area_multi = intersectionAreaMultiRec(rectangles)
                print(f"Площадь пересечения всех прямоугольников: {area_multi}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif number == 5:
            print("Выход")
            break
        else:
            print(f"Вы ввели {number}. Чтобы продолжить, введите число от 1 до 5.")

main() 
 
