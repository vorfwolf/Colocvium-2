#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#59. Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних чисел в ньому.
import numpy as np #імпортуємо numpy
import random #імпортуємо random

d = np.array([random.randint(-5, 10) for i in range(10)])
print(d)
print(np.unique(d)) #за домопогою фунцції unique() знаходимо всі унікальні числа з нашого масиву
print(len(np.unique(d))) #знаходимо кількість унікальних чисел
