#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#5. Створіть масив А [1..7] за допомогою генератора випадкових чисел і
#виведіть його на екран. Збільште всі його елементи в 2 рази.
import numpy as np #імпортуємо numpy
import random  #імпортуємо random

w = np.array([random.randint(-5, 10) for i in range(7)]) #масив з рандомних цілих чисел
print(w)
print(w*2) #збільшення всіх елементів масиву в 2 рази
