#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#56. Якщо в одновимірному масиві є три поспіль однакових елемента, то
#змінній r привласнити значення істина.
import numpy as np #імпортуємо numpy
import random #імпортуємо random

a = np.array([random.randint(1, 6) for i in range(15)])
print(a)

r = False #змінній r присвоєно значення хиби
for i in range(len(a)-2): #проходимося по нашому масиві
    if a[i] == a[i+1] == a[i+2]: #якщо значення будь-якого елементу буде дорівнювати значенню двох наступних
        #елементів масиву, то
        r = True #присвоюємо r значення істини
        print('true') #і виведемо
        break
    else: #в іншому випадку виводимо 'false' допоки ми не знайдемо три поспіль однакових елемента або
        #допоки не кінчиться масив
        print('false')
