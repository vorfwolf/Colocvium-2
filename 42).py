#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#42. Підрахувати кількість елементів одновимірного масиву, для яких
#виконується нерівність i*i<ai<i!
import numpy as np #імпортуємо numpy
import math #імпортуємо math
import random #імпортуємо random

q = np.array([random.randint(1, 100) for i in range(20)]) #масив з рандомних цілих чисел
print(q)

k = [] #пустий список
for i in range(len(q)): #проходимося по нашому масиві
    if q[i] > i*i and q[i] < math.factorial(i): #якщо є такі елементи одновимірного масиву, для яких
        # виконується нерівність i*i<ai<i!
        k.append(q[i]) #то добавляємо їх в список k
print(k)
print(len(k)) #підраховуємо та виводимо їхню кількість