#Функции isCorrectRect принимает аргумент rectangles
def isCorrectRec(rectangles):
    #Цикл for перебирает все элементы в rectangles и функция enumerate возвращает элемент rect и индекс элемента index
    for index, rect in enumerate(rectangles, start = 1):
        #Проверяем корректность прямоугольника
        if rect[0][0] >= rect[1][0] or rect[0][1] >= rect[1][1]:
            #Если прямоугольник некорректен, то вызывается исключение ValueError с сообщением номерf некорректного прямоугольника
            raise ValueError(f'Некорректный прямоугольник с номером {index}')
    #Если все прямоугольники корректны, функция возвращает True
    return True
