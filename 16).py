#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#16. Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
#масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
import numpy as np #імпортуємо numpy
import random #імпортуємо random

u = np.array([random.randint(10, 50) for i in range(15)]) #масив з рандомних цілих чисел
print(u)

kratni7 = [] #пустий список
m = 1
for i in u: #проходимося по нашому масиві
    if i % 7 == 0: #якщо елемент кратний 7, добавляємо цей елемент в список
        kratni7.append(i)
        m *= i #знаходимо добуток цих елементів
print(kratni7)
print(m)
