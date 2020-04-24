#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#38. Дані про направлення вітру (північний, південний, східний, західний) і
#силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
#південний вітер з силою, що перевищує 8 м / с.
import numpy as np #імпортуємо numpy

z = np.array(['північний', 'південний', 'західний', 'південний', 'східний',
              'східний', 'західний', 'південний', 'північний', 'західний']) #масив з направленнями вітру
print(z)
x = np.array([12, 6, 10, 13, 3, 7, 7, 11, 10, 5]) #масив з силаю вітру(м/с)
print(x)

c = 0 #кількість днів, коли дув південний вітер з силою, що перевищує 8 м / с.
for i in range(len(x)): #проходимося по нашому масиві з силою вітру
    if x[i] > 8 and z[i] == 'південний': #якщо вітер з силою більше 8 і з направленням 'південний', то
        c += 1 #добавляємо +1
print(c) #виводимо кількість днів, коли дув південний вітер з силою, що перевищує 8 м / с
