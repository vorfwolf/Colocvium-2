#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#52. Знайти найбільший елемент з елементів одновимірного масиву, що мають
#парний номер. Визначити, чи є він єдиним.
import numpy as np #імпортуємо numpy
import random #імпортуємо рандом

d = np.array([random.randint(1, 30) for i in range(30)]) #масив створений з рандомних цілих чисел
print(d)

k = [] #пустий список
for i in range(len(d)): #проходимося по нашому масиві
    if i % 2 == 0: #якщо елемент масиву має парний індекс, то
        k.append(d[i]) #добавляємо цей елемент масиву в пустий список
print(k)
print('Найбільший елемент з елементів одновимірного масиву, що мають парний номер: ', max(k)) #і знаходимо серед них
#найбільший елемент

a = 0 #кількість max(k)
for i in range(len(k)): #проходимося по нашому списку
    if max(k) == k[i]: #якщо наш максимальний елемент дорівнює елементу списку, то
        a += 1 #добавляємо +1

if a == 1: #якщо наш max(k) єдиний, виводимо
    print('Він є єдиним')
else: #якщо наш max(k) не єдиний, то виводимо
    print('Він не є єдиним')