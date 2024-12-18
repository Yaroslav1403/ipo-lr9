#Импортируем функцию для проверки корректности прямоугольников
from .isCorrectRect import isCorrectRect  
#Импортируем комбинации
from .itertools import combinations  

#Определяем собственное исключение для обработки ошибок с некорректными прямоугольниками
class RectCorrectError(Exception):
    pass

def intersectionAreaMultiRect(rectangles):
    
    def get_intersection(rects):
      
        #Находим максимальные координаты нижнего левого угла
        x1 = max(rect[0][0] for rect in rects)
        y1 = max(rect[0][1] for rect in rects)
        
        #Находим минимальные координаты верхнего правого угла
        x2 = min(rect[1][0] for rect in rects)
        y2 = min(rect[1][1] for rect in rects)
        
        #Проверяем, есть ли пересечение
        if x1 < x2 and y1 < y2:
            #Возвращаем координаты пересечения
            return [(x1, y1), (x2, y2)]  
        #Если пересечения нет, возвращаем None
        return None  
    
    def area(rect):
        
        if not rect:
            #Если прямоугольник некорректен, возвращаем 0
            return 0  
        #Вычисляем ширину
        width = rect[1][0] - rect[0][0]  
        #Вычисляем высоту
        height = rect[1][1] - rect[0][1]  
        #Возвращаем площадь
        return width * height  

    #Проверка корректности каждого прямоугольника
    for rect in rectangles:
        try:
            #Проверяем каждый прямоугольник отдельно
            isCorrectRect([rect])  
        except ValueError as e:
            #Если некорректный, выбрасываем исключение
            raise RectCorrectError(f"Некорректный прямоугольник: {e}")  

    #Переменная для хранения общей площади 
    total_area = 0  

    #Инициализируем текущее пересечение первым прямоугольником
    current_intersection = rectangles[0]
    
    #Проходим по остальным прямоугольникам и находим их пересечение с текущим
    for rect in rectangles[1:]:
        #Находим новое пересечение
        current_intersection = get_intersection([current_intersection, rect])  
        if current_intersection is None:
            #Если нет пересечения, возвращаем 0
            return 0  
    
    #Возвращаем площадь найденного пересечения
    return area(current_intersection)  