
import numpy as np

def game_score_1(number: int=1) -> int:
    '''
    Args:
        number (int, optional): Загаданное число. Default to 1.
    Returns:
        int: Число попыток
    '''
    
    count = 0 #счетчик
    predict_number_min = 1 #нижний предел
    predict_number_max = 101 #верхний предел
    
    while True:
        count+=1
        
        predict_number = (predict_number_max+predict_number_min)//2
        
        if number > predict_number:
            predict_number_min=predict_number #смешение нижнего предела и числа
            
        elif number < predict_number
            predict_number_max=predict_number #смешение верхнего предела и числа
            
        else:
            break
        
    return count

