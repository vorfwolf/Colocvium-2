#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#22. Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
#Заповнення масиву здійснити випадковими числами від 5 до 500.
import numpy as np #імпортуємо numpy
import random #імпортуємо random

s = np.array([random.randint(5, 500) for i in range(10)]) #масив з рандомних цілих чисел
print(s)

k = []
m = 1
for i in s: #проходимося по нашому масиві
    if i % 3 == 0 and i % 9 == 0: #якщо елемент кратний 3 і 9, то добавляємо його в список
        k.append(i)
        m *= i #знаходимо добуток цих елементів
print(k)

if m > 1:
    print(m)
else:
    print('Елементів, що кратні 3 і 9 немає, тому добутку теж')

