#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#15.Знайти суму парних елементів масиву цілих чисел. Розмірність масиву - 20.
#Заповнення масиву здійснити випадковими числами від 100 до 200.
import numpy as np #імпортуємо numpy
import random #імпортуємо random

u = np.array([random.randint(100, 200) for i in range(20)]) #масив з рандомних цілих чисел
print(u)

parni=[] #пустий список
for i in u: #проходимося по нашому масиві
    if i % 2 == 0: #якщо елемент парний, добавляємо цей елемент в список
        parni.append(i)
print(parni)
print(sum(parni)) #знаходимо суму цих елементів
