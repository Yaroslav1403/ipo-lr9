#Импорт функции isCorrectRect
from isCorrectRect import isCorrectRect 

def intersectionAreaRect(rectangles):
    #Переменная для хранения общей площади пересечения
    total_area = 0  
    
    #Проверка корректности входных данных
    try:
        #Проверяем, корректны ли прямоугольники
        isCorrectRect(rectangles)  
    except ValueError as error:
        #Если возникла ошибка, выводим ее сообщение и вызываем новую ошибку с комментарием
        raise ValueError("Некорректный прямоугольник: " + str(error))  

    #Получаем количество прямоугольников
    count = len(rectangles)  
    #Флаг для проверки наличия пересечений
    has_intersection = False  

    #Двойной цикл для перебора всех пар прямоугольников
    for i in range(count):
        for j in range(i + 1, count):
            #Извлекаем координаты первого прямоугольника
            x1, y1 = rectangles[i][0]  #Левый нижний угол
            x2, y2 = rectangles[i][1]  #Правый верхний угол

            #Извлекаем координаты второго прямоугольника
            x3, y3 = rectangles[j][0]  #Левый нижний угол
            x4, y4 = rectangles[j][1]  #Правый верхний угол

            #Вычисляем границы пересечения
            overlap_left = max(x1, x3)  #Левая граница пересечения
            overlap_top = min(y2, y4)    #Верхняя граница пересечения
            overlap_right = min(x2, x4)  #Правая граница пересечения
            overlap_bottom = max(y1, y3)  #Нижняя граница пересечения

            #Вычисляем ширину и высоту области пересечения
            overlap_width = overlap_right - overlap_left
            overlap_height = overlap_top - overlap_bottom

            #Проверяем, есть ли пересечение (ширина и высота больше нуля)
            if overlap_width > 0 and overlap_height > 0:
                #Добавляем площадь пересечения к общей площади
                total_area += overlap_width * overlap_height  
                #Устанавливаем флаг наличия пересечения
                has_intersection = True  

    if not has_intersection:
        #Если пересечений не было, возвращаем 0
        return 0  

    #Возвращаем общую площадь пересечений
    return total_area  
