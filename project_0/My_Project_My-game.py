"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np


number = np.random.randint(1, 101) # загадываем рандомное число, используя генератор рандомных чисел

def random_predict(number: int = 1) -> int:
    
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
        
        shot = round((min_number + max_number)/2)
        
        if shot > number:
            max_number = shot
        elif shot < number:
            min_number = shot
        else:
            print(f'Загаданное число: {number}')
            
            break # конец игры и выход из цикла
        
    return(count)

print(f'Компьютер отгадал это число за {random_predict(number)} попыток')