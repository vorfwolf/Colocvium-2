#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#40. Обчислити суму парних елементів одновимірного масиву до першого
#зустрінутого нульового елемента.
import numpy as np #імпортуємо numpy
import random #імпортуємо random

d = np.array([random.randint(-10, 10) for i in range(40)]) #масив з рандомних цілих чисел
print(d)

a = 0
k = [] #пустий список
for i in range(len(d)): #проходимося по нашому масиві
    if d[i] % 2 == 0: #якщо елемент парний, то добавляємо його в список k
        k.append(d[i])
        if d[i] == 0: #якщо ми зустрічаємо нульовий елемент, зупиняємо дію добавлення
            break

if a in k: #якщо нульовий елемент є в списку парних елементів, то видаляємо його
    k.remove(a)
    print(k)
elif a not in k: #якщо немає так і залишаємо
    print(k)
print(sum(k)) #за допомогою sum() знаходимо суму парних елементів масиву
