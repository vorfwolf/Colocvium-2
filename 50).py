#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#50. У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів виграшних квитків. Перевірте,
#чи є квиток з номером N виграшним.
import numpy as np #імпортуємо numpy
import random #імпортуємо random

d = np.array([random.randint(1, 100) for i in range(100)]) #масив з рандомних цілих чисел(лотерея зі 100 квитків)
print('Лотерея зі 100 квитків: ', d)
q = np.array([12, 31, 45, 43, 27, 99, 72, 88, 29, 75]) #масив з виграшними квитками

N = int(input('Введіть номер перевірочного квитка: '))
if N in d and N in q: #якщо наш перевірочний квиток є масиві d і є в масиві q, то квиток з номером N є виграшним
    #і ми виводимо
    print(f'Білет з номером {N} є виграшним')
else: #в іншому випадку виводимо
    print(f'Білет з номером {N} не є виграшним')
