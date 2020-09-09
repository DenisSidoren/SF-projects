#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
number = np.random.randint(1,101) #запускаем игру

def game_core(number):    #функция для подсчета колчиества попыток
    count = 1  #счётчик с "1" на случай попадания в яблочко с первой попытки
    for i in range(1,101,10):  #цикл с проходом по range укрупненно
        if i == number:
            break
        elif i < number:
            count += 1
            continue
        else:
            for j in range(i-9, i, 1):   #цикл, уточнящий внутри определенной десятки 
                count += 1
                if j == number:
                    break
        break
    return(count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    return(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

score_game(game_core)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




