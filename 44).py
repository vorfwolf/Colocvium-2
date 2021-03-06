#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
#своїм номером і при цьому кратні 3.
import numpy as np #імпортуємо numpy
import random #імпортуємо random

d = np.array([random.randint(1, 40) for i in range(40)]) #масив з рандомних цілих чисел
print(d)

k = [] #пустий список
for i in range(len(d)): #проходимося по нашому масиві
    if d[i] == i and d[i] % 3 == 0: #якщо в масиві є елементи, які збігаються зі своїми індексами
        #та є кратними 3,
        k.append(d[i]) #то добавляємо їх в список k
print(k)
print(len(k)) #підщитуємо та виводимо їхню кількість
