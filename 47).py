#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#47. У лінійному масиві знайти максимальний елемент. Вставте порядковий
#номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
import numpy as np #імпортуємо numpy
import random #імпортуємо random

d = np.array([random.randint(1, 100) for i in range(15)]) #масив з рандомних цілих чисел
print(d)

e = max(d) #максимальний елемент масив d

k = [] #пустий список
for i in range(len(d)): #проходимося по нашому масиві
    k.append(i) #добавляємо індекси елементів масиву в список, допоки не зустрінеться максимальний елемент
    if d[i] == e:
       break

r = [] #пустий список
for i in range(len(d)): #проходимося по нашому масиві
    r.append(i) #добавляємо індекси елементів масиву в список

z = [] #пустий список
for i in r: #добавляємо в список z індекси лише тих елементів, які йдуть після e
    if not (i in k):
        z.append(i)

print(np.append(np.append(np.delete(d, z), list(d).index(max(list(d)))), np.delete(d, k))) #видаляємо елементи, які
#йдуть після максимального елементу, вставляємо індекси максимального елемента зправа за ним і повертаємо
#елементи, які ми видалили, пересунувши їх вправо на  1 позицію
