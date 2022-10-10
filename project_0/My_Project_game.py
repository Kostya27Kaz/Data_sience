"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

a = int(input('Введите начальное число: '))
b = int(input('Введите конечное число: '))

number = np.random.randint(a, b) # загадываем рандомное число, используя генератор рандомных чисел

def random_predict(number) -> int:
    
    """Компьютер угадывает рандомное число

    Args:
        number (int, optional): Загаданное число.
        
    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 100

    while True:
        
        count += 1
        
        md = round((min_number + max_number)//2)
        
        if md > number:
            max_number = md
        elif md < number:
            min_number = md
        else:
            print(f'Компьютер загадал число: {number}')
            
            break # конец игры и выход из цикла
        
    return(count)

print(f'Компьютер отгадал это число за {random_predict(number)} попыток')