#Импортируем функцию для проверки корректности прямоугольников
from .IsCorrectRect import isCorrectRec 
#Импортируем функцию для генерации комбинаций
from itertools import combinations  

def intersectionAreaMultiRec(rectangles):
    #Вложенная функция для нахождения пересечения нескольких прямоугольников
    def get_intersection(rects):
        
        #Находим максимальные координаты левого нижнего угла
        x1 = max(rect[0][0] for rect in rects)
        y1 = max(rect[0][1] for rect in rects)
        
        #Находим минимальные координаты правого верхнего угла
        x2 = min(rect[1][0] for rect in rects)
        y2 = min(rect[1][1] for rect in rects)
        
        #Проверяем, существует ли пересечение
        if x1 < x2 and y1 < y2:
            #Возвращаем координаты пересечения
            return [(x1, y1), (x2, y2)]  
        #Если пересечения нет, возвращаем None
        return None  
    
    #Вложенная функция для вычисления площади прямоугольника
    def area(rect):
        if not rect:
            #Если прямоугольник не существует, площадь равна 0
            return 0 
        
        #Ширина равна разности x-координат
        width = rect[1][0] - rect[0][0]  
        #Высота равна разности y-координат
        height = rect[1][1] - rect[0][1]  
        #Возвращаем площадь
        return width * height  

    #Переменная для хранения общей площади пересечений
    total_area = 0  
    #Список для хранения всех найденных пересечений
    all_intersections = []  
    
    #Перебираем все комбинации пар прямоугольников
    for combination in combinations(rectangles, 2):
        #Находим пересечение для пары
        intersection = get_intersection(combination)  
        #Если пересечение существует
        if intersection:  
            #Добавляем его в список
            all_intersections.append(intersection)  

    #Используем принцип включения-исключения для вычисления общей площади
    for k in range(1, len(all_intersections) + 1):
        #Определяем знак для текущей комбинации (положительный или отрицательный)
        sign = (-1) ** (k + 1)  
        for combination in combinations(all_intersections, k):
            intersection = get_intersection(combination)  #Находим пересечение для текущей комбинации
            #Добавляем или вычитаем площадь из общей площади
            total_area += sign * area(intersection)  

    #Возвращаем общую площадь пересечений
    return total_area  
