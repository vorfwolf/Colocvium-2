#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з однаковими значеннями.
import collections #імпортуємо collections
import numpy as np #імпортуємо numpy

w = np.array([1, 3, 4, 6, 5, 62, 6, 3, 6, 12, 42, 6, 5, 7, 8, 2, 42, 31, 42, 1]) #масив з рандомних чисел
print(w)

c = collections.Counter(w) #за допомогою collections.Counter() зіщитуємо кількість кожного з елементів
print(c)
